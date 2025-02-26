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

def by_item(table:pd.DataFrame) -> pd.DataFrame:
    try:
        while True:
            item = validate.string_answer('Digite o nome do produto: ')
            print()
            item_to_delete = get_data.specific_row(table, ColumnName.ITEM.value, item)
            if item_to_delete.empty:
                print('O produto não foi encontrado. Digite um nome válido.\n')
            else:
                table = table.drop(table[table[ColumnName.ITEM.value] == item].index)
                print('Produto deletado com sucesso!\n')
                break
        return table

    except:
        message.system.error()

def by_category(table:pd.DataFrame) -> pd.DataFrame:
    try:
        while True:
            category = validate.string_answer('Digite a categoria: ')
            print()
            category_to_delete = get_data.specific_row(table, ColumnName.CATEGORY.value, category)
            if category_to_delete.empty:
                print('A categoria não foi encontrada. Digite uma categoria válida.\n')
            else:
                table = table.drop(table[table[ColumnName.CATEGORY.value] == category].index)
                print('Categoria deletada com sucesso!\n')
                break
        return table

    except:
        message.system.error()

def by_price(table:pd.DataFrame) -> pd.DataFrame:
    try:
        while True:
            min_value = validate.min_price_value()
            print()
            max_value = validate.max_price_value(min_value)
            print()
            price_to_delete = get_data.specific_row(table=table, column_to_filter=ColumnName.PRICE.value, min_value=min_value, max_value=max_value)
            if price_to_delete.empty:
                print('Os preços não foram encontrados. Digite preços válidos.\n')
            else:
                table = table.drop(table[(table[ColumnName.PRICE.value] >= min_value) & (table[ColumnName.PRICE.value] <= max_value)].index)
                print('Preços deletados com sucesso!\n')
                break
        return table

    except:
        message.system.error()

def by_quantity(table:pd.DataFrame) -> pd.DataFrame:
    try:
        while True:
            min_value = validate.min_quantity_value()
            print()
            max_value = validate.max_quantity_value(min_value)
            print()
            quantity_to_delete = get_data.specific_row(table=table, column_to_filter=ColumnName.QUANTITY.value, min_value=min_value, max_value=max_value)
            if quantity_to_delete.empty:
                print('As quantidades não foram encontradas. Digite quantidades válidas.\n')
            else:
                table = table.drop(table[(table[ColumnName.QUANTITY.value] >= min_value) & (table[ColumnName.QUANTITY.value] <= max_value)].index)
                print('Quantidades deletadas com sucesso!\n')
                break
        return table

    except:
        message.system.error()
