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

import pandas as pd
import numpy as np
import calendar

from geopy.distance import geodesic

import os
if airport_icao == "ESSA":
    from constants_ESSA import *
elif airport_icao == "ESGG":
    from constants_ESGG import *
elif airport_icao == "EIDW":
    from constants_EIDW import *
elif airport_icao == "LOWW":
    from constants_LOWW import *

DATA_DIR = os.path.join("data", airport_icao)
DATA_DIR = os.path.join(DATA_DIR, year)
INPUT_DIR = os.path.join(DATA_DIR, "osn_" + airport_icao + "_tracks_" + year)
OUTPUT_DIR = os.path.join(DATA_DIR, "osn_" + airport_icao + "_tracks_50NM_" + year)

if not os.path.exists(INPUT_DIR):
    os.makedirs(INPUT_DIR)
    
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def get_all_tracks(csv_input_file):

    df = pd.read_csv(os.path.join(INPUT_DIR, csv_input_file), sep=' ',
                    names = ['flightId', 'sequence', 'origin', 'endDate', 'callsign', 'icao24', 'date', 'time', 'timestamp',
                             'lat', 'lon', 'baroAltitude'],
                    index_col=[0,1],
                    dtype={'flightId':str, 'sequence':int, 'time':str, 'endDate':str, 'date':str})
    
    return df


# start from the last waypoint outside 50NM circle
def get_tracks_inside_50NM_circle(month, week, tracks_df, csv_output_file):

    tracks_inside_50NM_circle_df = pd.DataFrame()

    number_of_flights = len(tracks_df.groupby(level='flightId'))

    count = 1
    for flight_id, new_df in tracks_df.groupby(level='flightId'):
        print(airport_icao, year, month, week, number_of_flights, count, flight_id)
        count = count + 1
        entry_point_index = get_entry_point_index(flight_id, new_df)
        
        if entry_point_index==-1:
            print("entry point index == -1")
            continue
        
        if entry_point_index !=0:
            entry_point_index = entry_point_index -1
        
        new_df_inside_50NM_circle = new_df.iloc[entry_point_index:].copy()
        
        # reassign sequence
        new_df_inside_50NM_circle.reset_index(drop=False, inplace=True)
        new_df_inside_50NM_circle_length = len(new_df_inside_50NM_circle)
        
        sequence_list = list(range(new_df_inside_50NM_circle_length))
        
        new_df_inside_50NM_circle.drop(['sequence'], axis=1, inplace=True)
        
        new_df_inside_50NM_circle['sequence'] = sequence_list
        
        new_df_inside_50NM_circle = new_df_inside_50NM_circle[['flightId', 'sequence', 'origin', 'endDate', 'callsign', 'icao24', 'date', 'time', 
                                               'timestamp', 'lat', 'lon', 'baroAltitude']]
        
        
        #if new_df.iloc[entry_point_index-1]['date'] == new_df.iloc[-1]['date']:
        tracks_inside_50NM_circle_df = tracks_inside_50NM_circle_df.append(new_df_inside_50NM_circle)
        
    tracks_inside_50NM_circle_df.to_csv(os.path.join(OUTPUT_DIR, csv_output_file), sep=' ', encoding='utf-8', float_format='%.6f', header=None, index=False)


def get_entry_point_index(flight_id, new_df):
    
    lat = 0.0
    lon = 0.0
    for seq, row in new_df.groupby(level='sequence'):
        lat = row.loc[(flight_id, seq)]['lat']
        lon = row.loc[(flight_id, seq)]['lon']
        #if (check_50NM_circle_contains_point(Point(row.loc[(flight_id, seq)]['lon'], row.loc[(flight_id, seq)]['lat']))):
        if (check_50NM_circle_contains_point((row.loc[(flight_id, seq)]['lat'], row.loc[(flight_id, seq)]['lon']))):
            return seq
    print(lat, lon)
    return -1


def check_50NM_circle_contains_point(point):
    
    central_point = (central_lat, central_lon)
    distance = geodesic(central_point, point).meters
    
    if distance < 50*1852:
        return True
    else:
        return False


def extract_TMA_part(month, week):
    
    input_filename = 'osn_' + airport_icao + '_tracks_' + year + '_' + month + '_week' + str(week) + '.csv'
    
    all_tracks_df = get_all_tracks(input_filename)
        
    output_filename = 'osn_' + airport_icao + '_tracks_50NM_' + year + '_' + month + '_week' + str(week) + '.csv'
    
    get_tracks_inside_50NM_circle(month, week, all_tracks_df, output_filename)
    

import time
start_time = time.time()

from multiprocessing import Process


for month in months:

    procs = [] 
    
    number_of_weeks = (5, 4)[month == '02' and not calendar.isleap(int(year))]
        
    for week in range(0, number_of_weeks):
        
        proc = Process(target=extract_TMA_part, args=(month, week + 1,))
        procs.append(proc)
        proc.start()
        
        
    # complete the processes
    for proc in procs:
        proc.join()
            
print((time.time()-start_time)/60)