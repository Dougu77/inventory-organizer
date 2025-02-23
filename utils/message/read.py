import pandas as pd
from utils.enum import ColumnName
from utils import message
from utils import validate
from utils import get_data
from utils import constants

def options() -> int:
    try:
        print('Quais dados deseja ver?\n')
        print('[ 1 ] Tabela completa')
        print('[ 2 ] Produto específico')
        print('[ 3 ] Categoria específica')
        print('[ 4 ] Preço específico')
        print('[ 5 ] Quantidade específica')
        print('[ 6 ] Mais condições')
        print('[ 7 ] Voltar\n')
        choice = validate.choice_number(7)
        print()
        return choice
    except:
        message.system.error()
        return 7

def full_table(table:pd.DataFrame) -> None:
    try:
        print(table)
        print()
    except:
        message.system.error()

def specific_rows(table:pd.DataFrame, column:str) -> None:
    try:
        if column in [ColumnName.PRICE.value, ColumnName.QUANTITY.value]:
            if column == ColumnName.PRICE.value:
                min_value = validate.min_price_value()
                print()
                max_value = validate.max_price_value(min_value)
            else:
                min_value = validate.min_quantity_value()
                print()
                max_value = validate.max_quantity_value(min_value)
            value_data = get_data.specific_row(table=table, column_to_filter=column, min_value=min_value, max_value=max_value)
        else:
            value_name = validate.string_answer(constants.read_question[column])
            value_data = get_data.specific_row(table=table, column_to_filter=column, value=value_name)
        print()
        if value_data.empty:
            print('A pesquisa não retornou resultados.')
        else:
            print(value_data)
        print()
    except:
        message.system.error()
