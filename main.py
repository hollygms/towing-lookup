from config import dt, TOWING_COLUMN, VIN_COLUMN, SOURCE_COLUMN
from ford import get_vin_towing
from validate_vin import get_validated_dataframe
from filter_data import get_filtered_vins


if __name__ == '__main__':

    #validating the vins via api and updating the dataframe
    dt = get_validated_dataframe(dt)

    #getting dictionary of vins with the towing and source
    ford_vin_dict = get_vin_towing(get_filtered_vins(dt))

    #updating the dataframe with the towing and source
    for key in ford_vin_dict:
        index = dt.loc[dt[VIN_COLUMN] == key].index
        dt.loc[index, TOWING_COLUMN] = ford_vin_dict[key][0]
        dt.loc[index, SOURCE_COLUMN] = ford_vin_dict[key][1]

    dt.to_csv('New Data.csv', index=False)

    