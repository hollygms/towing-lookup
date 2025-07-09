from config import MANUFACTURER, YEAR_START, YEAR_END, dt

def filter_vins():
    valid_vin = []
    for index, row in dt.iterrows():
        if dt.loc[index, 'Towing Capacity (lbs)'] != 'VIN ERROR':
            if row['Manufacturer'] == MANUFACTURER and YEAR_START <= int(row['Construct Year']) <= YEAR_END:
                valid_vin.append(row['VIN'])
    return valid_vin

