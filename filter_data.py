from config import MANUFACTURER, YEAR_START, YEAR_END, dt, TOWING_COLUMN, VIN_COLUMN

def filter_vins():
    """Returns a list of VIN's that valid, by the MANUFACTURER and within the year start and year end"""
    valid_vin = []
    for index, row in dt.iterrows():
        if dt.loc[index, TOWING_COLUMN] != 'VIN ERROR':
            if row['Manufacturer'] == MANUFACTURER and YEAR_START <= int(row['Construct Year']) <= YEAR_END:
                valid_vin.append(row[VIN_COLUMN])
    return valid_vin

