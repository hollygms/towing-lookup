from config import dt, CSV_FILE, FORD_URL
from ford import get_ford_towing
from validate_vin import check_valid_vins

check_valid_vins()
vin_towing = get_ford_towing()

for key, value in vin_towing.items():
    dt.loc[dt['VIN'] == key, 'Towing Capacity (lbs)'] = value
    dt.loc[dt['VIN'] == key, 'Source'] = FORD_URL

dt.to_csv(CSV_FILE, index=False)