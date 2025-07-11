from config import dt, NHTSA_URL, CSV_FILE, VIN_COLUMN, ENGINE_COLUMN, TOWING_COLUMN
import requests

def check_nhtsa_api():
    """Loops through the database's VIN column and runs each vin through the NHTSA API.
    Updates Towing and Engine columns to VIN ERROR if a 400 error is received from API.
    Otherwise, just updates the engine and fuel type"""
    for i, vin in enumerate(dt[VIN_COLUMN], 1):
        if type(vin) == str and vin != VIN_COLUMN:  # skipping empty vin columns or repeat header names
            response = requests.get(f'{NHTSA_URL}/{vin}?format=json').json()
            validation = response['Results'][0]['ErrorCode']
            engine = response['Results'][0]['DisplacementL']
            fuel = response['Results'][0]['FuelTypePrimary']

            # checks for error code
            if validation == '1,400':
                dt.at[i-1, TOWING_COLUMN] = 'VIN ERROR'
                dt.at[i-1, ENGINE_COLUMN] = 'VIN ERROR'
            else:
                dt.at[i-1, ENGINE_COLUMN] = f'{engine}L/{fuel}'

        if i % 50 == 0:  # quick progress check
            print(f'Processed {i} VINs')

    dt.to_csv(CSV_FILE, index=False)


check_nhtsa_api()