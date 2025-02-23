import pandas as pd
from utils.enum import ColumnName
from utils import message
from utils import validate
from utils import get_data

def options() -> int:
    try:
        print('Qual o critério para deletar?\n')
        print('[ 1 ] Nome do produto')
        print('[ 2 ] Categoria')
        print('[ 3 ] Preço')
        print('[ 4 ] Quantidade')
        print('[ 5 ] Mais condições')
        print('[ 6 ] Voltar\n')
        choice = validate.choice_number(6)
        print()
        return choice
    except:
        message.system.error()
        return 6

def row_by_item(table:pd.DataFrame) -> pd.DataFrame:
    try:
        while True:
            item = validate.string_answer('Digite o nome do produto: ')
            print()
            item_to_delete = get_data.specific_row(table, ColumnName.ITEM.value, item)
            if item_to_delete.empty:
                print('O produto não foi deletado. Digite um nome válido.\n')
            else:
                table = table.drop(table[table[ColumnName.ITEM.value] == item].index)
                print('Produto deletado com sucesso!\n')
                break
        return table

    except:
        message.system.error()
