'''
    The Purpose of this script is to download 200 hPa U, V, and relative
    vorticity over colorado from ERA5 for the year 2022.
'''

#imports go here
import cdsapi
import os

#set data paht and navigate to it
data_dir = '/Users/justinhudson/Documents/HW/ATS_780/Homework_2/DATA'
os.chdir(data_dir)

#call the copernicus API to get the data
c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'u_component_of_wind', 'v_component_of_wind', 'vorticity',
        ],
        'pressure_level': '200',
        'year': ['2021','2022',
        ],
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
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': [
            42, -110, 36,
            -100,
        ],
    },
    'ERA5_200hpa_U_V_relVort_Colorado_2021_2022.nc')