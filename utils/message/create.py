import pandas as pd
from utils import message
from utils import validate

def row(table:pd.DataFrame) -> None:
    try:
        item = validate.string_answer('Digite o nome do produto: ')
        print()
        category = validate.string_answer('Digite a categoria: ')
        print()
        price = validate.create_or_update_price()
        print()
        quantity = validate.create_or_update_quantity()
        print()
        table.loc[len(table)] = [item, category, price, quantity]
        print('Produto adicionado com sucesso!\n')
    except:
        message.system.error()
