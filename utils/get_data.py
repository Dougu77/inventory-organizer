from utils import message
from utils import validate
from utils.enum import ColumnName
import pandas as pd
import os
import glob

def excel_path() -> str:
    base_folder = os.path.dirname(__file__)
    excel_folder = os.path.join(base_folder, '../excel')
    file = glob.glob(os.path.join(excel_folder, '*.xlsx'))[0]
    path = os.path.abspath(file)
    return path

def table() -> pd.DataFrame:
    try:
        table = pd.read_excel(excel_path(), index_col=False)
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

def row_to_update(table:pd.DataFrame) -> pd.Series:
    while True:
        item = validate.string_answer('Digite o nome do produto: ')
        print()
        item_to_update = specific_row(table, ColumnName.ITEM.value, item)
        if item_to_update.empty:
            print('O produto não foi encontrado. Digite um nome válido.\n')
        else:
            break
    return item_to_update

def column_by_choice_number(choice:int) -> str:
    match choice:
        case 1:
            column = ColumnName.ITEM.value
        case 2:
            column = ColumnName.CATEGORY.value
        case 3:
            column = ColumnName.PRICE.value
        case 4:
            column = ColumnName.QUANTITY.value
    return column
