import pandas as pd
from config import NHTSA_URL, VIN_COLUMN, ENGINE_COLUMN, TOWING_COLUMN, dt
import requests

def get_validated_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Loops through the database's VIN column and runs each vin through the NHTSA API.
    Updates Towing and Engine columns to VIN ERROR if a 400 error is received from API.
    Otherwise, just updates the engine and fuel type"""
    #drops all blank vin numbers
    dt.dropna(subset=[VIN_COLUMN], inplace=True) 

    #selects only the vins that have nothing in the engine column
    missing_engine_dt = dt[dt[ENGINE_COLUMN].isna()]
    
    for i, vin in enumerate(missing_engine_dt[VIN_COLUMN]):
        response = requests.get(f'{NHTSA_URL}/{vin}?format=json').json()
        validation = response['Results'][0]['ErrorCode']
        engine = response['Results'][0]['DisplacementL']
        fuel = response['Results'][0]['FuelTypePrimary']
 
        # checks for vin error code
        if validation == '1,400':
            dt.at[i, TOWING_COLUMN] = 'VIN ERROR'
            dt.at[i, ENGINE_COLUMN] = 'VIN ERROR'
        else:
            dt.at[i, ENGINE_COLUMN] = f'{engine}L/{fuel}'

        if i+1 % 50 == 0:  # quick progress check
            print(f'Processed {i} VINs')

    return dt

#get_validated_dataframe(df=dt)
