import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
#        'product_type': 'reanalysis',
        'product_type': 'ensemble_members',
        'format': 'netcdf',
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind',
            'instantaneous_10m_wind_gust',
            'cloud_base_height', 'low_cloud_cover',
            'total_cloud_cover',
            'convective_available_potential_energy', 'convective_precipitation',
            'total_precipitation',
            'snowfall', 'snow_depth',
        ],
        'area': '62/17/62/17',
        'year': '2019',
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': [
            '00:00', #'01:00', '02:00',
            '03:00', #'04:00', '05:00',
            '06:00', #'07:00', '08:00',
            '09:00', #'10:00', '11:00',
            '12:00', #'13:00', '14:00',
            '15:00', #'16:00', '17:00',
            '18:00', #'19:00', '20:00',
            '21:00', #'22:00', '23:00',
        ],
    },
    'data/Sundsvall/Sundsvall_2019_ensemble.nc')
