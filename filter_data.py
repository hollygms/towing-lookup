import pandas as pd

from config import MANUFACTURER, YEAR_START, YEAR_END, TOWING_COLUMN, VIN_COLUMN

def get_filtered_vins(dt: pd.DataFrame) -> list[str]:
    """Returns a list of VIN's that valid, by the MANUFACTURER and within the year start and year end"""
    
    #filters dt by the manufactuerer and date range
    ford_df = dt[dt.Manufacturer.str.upper() == 'FORD'].loc[(dt['Construct Year'] <= YEAR_END) & (dt['Construct Year'] >= YEAR_START)]

    #drops anything that has VIN ERROR already in the towing column
    ford_df = ford_df.drop(ford_df[ford_df[TOWING_COLUMN] == 'VIN ERROR'].index)

    #returns the list of vins
    valid_vins = ford_df.VIN.to_list()
    
    return valid_vins

