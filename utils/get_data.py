import pandas as pd
import os

def table() -> pd.DataFrame:
    file = 'Estoque.xlsx'
    folder = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(folder, '..', file))
    table = pd.read_excel(path, index_col=False)
    return table

def specific_row(table:pd.DataFrame, column_to_filter:str, value:str) -> pd.Series:
    return table.loc[table[column_to_filter] == value.strip()]

def specific_column(table:pd.DataFrame, row:str) -> pd.Series:
    return table[row]
