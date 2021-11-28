# -*- coding: utf-8 -*-
"""

Functions to download, read and parse data from different sources:

1.ERA5 reanalysis
2. ...
    
"""
import cdsapi
import os, time
from pathlib import Path

# For ERA5, ERA5 Land
def download_ERA5_hourly_data(outpath = '',
                              outfilenamecore = 'ERA5Land_location_hourly_prcp_',
                              dataset = 'reanalysis-era5-land',
                              varname ="total_precipitation",
                              start_year = 1950, 
                              end_year = 2022,
                              area = [90, -180, -90, 180], #: N,W,S,E,
                              grid =  [0.1, 0.1] # lat/lon grid. Default: 0.1 x 0.1 for ERA5Land, 0.25 x 0.25 for ERA5
                               ):
    for i in range(start_year, end_year):
    	y = str(i)
    	print(y)
    
    	c = cdsapi.Client()
    
    	r = c.retrieve(
            dataset,
            {
                'variable': varname,
                'year': y,
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
                'format': 'netcdf',
                'area': area,
                'grid': grid, 
            })
    	
    return r.download(outpath + "/", outfilenamecore, + y + ".nc")

def main() -> None:
    """Run everything"""

    # parse command line arguments
    parser = argparse.ArgumentParser(description='Input info for download')
    parser.add_argument("--varname", type=str)
    parser.add_argument("--endyear", type=int)
    parser.add_argument("-o", "--outfile", type=str)
    args = parser.parse_args()
    

    
    download_ERA5_hourly_data(outpath = '',
                              outfilenamecore = [args.outfile],
                              varname = [args.varname],
                              start_year = start_year,
                              end_year = [args.endyear],
                              #: N,W,S,E
                              grid = [0.1, 0.1], # lat/lon grid. Default: 0.1 x 0.1 for ERA5Land, 0.25 x 0.25 for ERA5
                               )
    
if __name__ == "__main__":
    main()
