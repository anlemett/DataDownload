##############################################################################

#airport_icao = "ESSA"
#airport_icao = "ESGG"
airport_icao = "EIDW" # Dublin
#airport_icao = "LOWW" # Vienna

arrival = True

year = '2019'

#months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
months = ['10']

##############################################################################

import os

DATA_DIR = os.path.join("data", airport_icao)
DATA_DIR = os.path.join(DATA_DIR, year)
INPUT_DIR = os.path.join(DATA_DIR, "osn_" + airport_icao + "_states_close_to_50NM_fixed_lat_lon_" + year)
OUTPUT_DIR = os.path.join(DATA_DIR, "osn_" + airport_icao + "_states_50NM_raw_" + year)

if not os.path.exists(INPUT_DIR):
    os.makedirs(INPUT_DIR)
    
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


import pandas as pd
import numpy as np
import calendar

from geopy.distance import geodesic

if airport_icao == "ESSA":
    from constants_ESSA import *
elif airport_icao == "ESGG":
    from constants_ESGG import *
elif airport_icao == "EIDW":
    from constants_EIDW import *
elif airport_icao == "LOWW":
    from constants_LOWW import *

def get_states_inside_50NM(states_df, month, week):
    
    filename = 'osn_' + airport_icao + '_states_50NM_raw_all_' + year + '_' + month + '_week' + str(week) + '.csv'
     
    full_output_filename = os.path.join(OUTPUT_DIR, filename)

    states_inside_TMA_df = pd.DataFrame()

    number_of_flights = len(states_df.groupby(level='flightId'))
    count = 1
    for flight_id, flight_df in states_df.groupby(level='flightId'):
        print(airport_icao, year, month, week, number_of_flights, count)
        count = count + 1
        first_point_index = get_first_point_index(flight_id, flight_df)
        
        if first_point_index==-1:
            continue
        
        new_df_inside_TMA = flight_df.loc[flight_df.index.get_level_values('sequence') >= first_point_index]
        
        new_df_inside_TMA.reset_index(drop=False, inplace=True)
        new_df_inside_TMA.set_index(['flightId'], inplace=True)
        
        # reassign sequence
        new_df_inside_TMA_length = len(new_df_inside_TMA)
        
        sequence_list = list(range(new_df_inside_TMA_length))
        
        new_df_inside_TMA = new_df_inside_TMA.sort_values(by=['timestamp'])
        
        new_df_inside_TMA.drop(['sequence'], axis=1, inplace=True)
        
        new_df_inside_TMA['sequence'] = sequence_list
        
        new_df_inside_TMA = new_df_inside_TMA[['sequence', 'timestamp', 'lat', 'lon', 'altitude', 'velocity', 'beginDate', 'endDate']]
        #if new_df.iloc[entry_point_index-1]['date'] == new_df.iloc[-1]['date']:
        states_inside_TMA_df = states_inside_TMA_df.append(new_df_inside_TMA)
        
    
    number_of_flights = len(states_inside_TMA_df.groupby(level='flightId'))
    
    states_inside_TMA_df.to_csv(full_output_filename, sep=' ', encoding='utf-8', float_format='%.6f', header=None, index=True)



def get_first_point_index(flight_id, flight_df):
    
    lat = 0
    lon = 0
    for seq, row in flight_df.groupby(level='sequence'):
        lat = row.loc[(flight_id, seq)]['lat']
        lon = row.loc[(flight_id, seq)]['lon']
        if (check_50NM_circle_contains_point((lat, lon))):
            #print(seq)
            #print(lon, lat)
            return seq
    
    print("-1", lat, lon)
    return -1


def check_50NM_circle_contains_point(point):
    central_point = (central_lat, central_lon)
    distance = geodesic(central_point, point).meters
    
    if distance < 50*1852:
        return True
    else:
        return False



import time
start_time = time.time()


for month in months:
    
    number_of_weeks = (5, 4)[month == '02' and not calendar.isleap(int(year))]
        
    for week in range(0, number_of_weeks):
        
        filename = 'osn_' + airport_icao + '_states_close_to_50NM_' + year + '_' + month + '_week' + str(week + 1) + '.csv'
        
        full_input_filename = os.path.join(INPUT_DIR, filename)
        
        df = pd.read_csv(full_input_filename, sep=' ',
                    names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'altitude', 'velocity', 'beginDate', 'endDate'],
                    index_col=[0,1],
                    dtype={'flightId':str, 'sequence':int, 'timestamp':str, 'lat':float, 'lon':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})

        get_states_inside_50NM(df, month, week + 1)

print((time.time()-start_time)/60)
