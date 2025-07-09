from config import dt, NHTSA_URL, CSV_FILE
import requests

def check_valid_vins():
    for vin in dt['VIN']:
        if type(vin) == str and vin != 'VIN':  #weird column names in the middle of the data, skipping them entirely
            response = requests.get(f'{NHTSA_URL}/{vin}?format=json').json()
            validation = response['Results'][0]['ErrorCode']

            if validation == '1,400':
                dt.loc[dt['VIN'] == vin, dt['Towing Capacity (lbs)']] = 'VIN ERROR'

    dt.to_csv(CSV_FILE, index=False)