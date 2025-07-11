import pandas as pd

MANUFACTURER = 'Ford'
YEAR_START = 2020
YEAR_END = 2025
CSV_FILE = input('Enter file name:\n')
TOWING_COLUMN = 'Towing Capacity (lbs)'
ENGINE_COLUMN = 'NHTSA Engine size/fuel'
VIN_COLUMN = 'VIN'
SOURCE_COLUMN = 'Source'



dt = pd.read_csv(CSV_FILE)

FORD_URL = 'https://www.ford.com/support/towing-calculator'
NHTSA_URL = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValuesExtended/'
