import pandas as pd

MANUFACTURER = 'Ford'
YEAR_START = 2020
YEAR_END = 2025
CSV_FILE = 'data.csv'
TOWING_COLUMN = 'Towing Capacity (lbs)'
ENGINE_COLUMN = 'NHTSA Engine size/fuel'
VIN_COLUMN = 'VIN'
SOURCE_COLUMN = 'Source'



dt = pd.read_csv(CSV_FILE)
dt[TOWING_COLUMN] = dt[TOWING_COLUMN].astype('object') #errors get added as a string, converting to avoid an error

FORD_URL = 'https://www.ford.com/support/towing-calculator'
NHTSA_URL = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValuesExtended/'
