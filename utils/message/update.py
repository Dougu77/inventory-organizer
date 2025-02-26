import pandas as pd
from utils.enum import ColumnName
from utils import message
from utils import validate
from utils import get_data

def options() -> int:
    try:
        print('O que você deseja atualizar?\n')
        print('[ 1 ] Item (Qualquer dado do item)')
        print('[ 2 ] Categoria')
        print('[ 3 ] Preço')
        print('[ 4 ] Quantidade')
        print('[ 5 ] Voltar\n')
        choice = validate.choice_number(5)
        print()
        return choice
    except:
        message.system.error()
        return 5

def item(table:pd.DataFrame) -> None:
    try:
        data = get_data.row_to_update(table)
        print(data)
        print('\nQual dado deseja alterar?\n')
        print('[ 1 ] Nome do item')
        print('[ 2 ] Categoria')
        print('[ 3 ] Preço')
        print('[ 4 ] Quantidade\n')
        choice = validate.choice_number(4)
        print()

        match choice:
            case 1:
                new_value = validate.string_answer('Digite o nome do produto: ')
                column = ColumnName.ITEM.value
            case 2:
                new_value = validate.string_answer('Digite a categoria: ')
                column = ColumnName.CATEGORY.value
            case 3:
                new_value = validate.create_or_update_price()
                column = ColumnName.PRICE.value
            case 4:
                new_value = validate.create_or_update_quantity()
                column = ColumnName.QUANTITY.value

        old_item_name = data.at[data.index[0], ColumnName.ITEM.value]
        table.loc[table[ColumnName.ITEM.value] == old_item_name, column] = new_value
        print('\nProduto atualizado com sucesso!\n')

    except:
        message.system.error()
