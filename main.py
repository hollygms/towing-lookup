from config import dt, CSV_FILE, FORD_URL, TOWING_COLUMN, VIN_COLUMN, SOURCE_COLUMN
from ford import get_ford_towing
from validate_vin import check_nhtsa_api


if __name__ == '__main__':
    check_nhtsa_api()
    vin_towing = get_ford_towing()

    for key, value in vin_towing.items():
        dt.loc[dt[VIN_COLUMN] == key, TOWING_COLUMN] = value
        dt.loc[dt[VIN_COLUMN] == key, SOURCE_COLUMN] = FORD_URL

    dt.to_csv(CSV_FILE, index=False)