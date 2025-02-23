from utils import message
import pandas as pd
import os

def table() -> pd.DataFrame:
    file = 'Estoque.xlsx'
    folder = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(folder, '..', file))
    try:
        table = pd.read_excel(path, index_col=False)
    except:
        message.system.table_not_found()
        table = pd.DataFrame()
    return table

def specific_row(table:pd.DataFrame, column_to_filter:str, value:str='', min_value:float=-1, max_value:float=-1) -> pd.Series:
    if min_value == -1 and max_value == -1:
        return table.loc[table[column_to_filter] == value.strip()]
    else:
        return table.loc[(table[column_to_filter] >= min_value) & (table[column_to_filter] <= max_value)]

def specific_column(table:pd.DataFrame, row:str) -> pd.Series:
    return table[row]
