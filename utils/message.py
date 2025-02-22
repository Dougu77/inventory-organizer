import pandas as pd
from utils.enum import ColumnName
from utils import validate
from utils import get_data
from utils import constants

def start() -> None:
    print('-' * 109)
    print(f'{"-" * 50} Estoque {"-" * 50}')
    print('-' * 109)
    print('\n- Esse programa ajuda na organização do estoque da loja.')
    print('- Visualize e edite os dados como desejar.')
    print('- Digite somente o número da opção que desejar.\n')

def table_not_found() -> None:
    print('A tabela não foi encontrada.\n')

def choice_crud() -> int:
    print('O que deseja fazer?\n')
    print('[ 1 ] Ver dados')
    print('[ 2 ] Adicionar produto')
    print('[ 3 ] Modificar produto')
    print('[ 4 ] Deletar produto')
    print('[ 5 ] Sair do programa\n')
    choice = validate.choice_number(5)
    print()
    return choice

def read() -> int:
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

def read_full_table(table:pd.DataFrame) -> None:
    print(table)
    print()

def read_specific_rows(table:pd.DataFrame, column:str) -> None:
    if column in [ColumnName.PRICE.value, ColumnName.QUANTITY.value]:
        if column == ColumnName.PRICE.value:
            min_value = validate.float_answer('Digite o preço mínimo: ')
            print()
            max_value = validate.float_answer('Digite o preço máximo: ')
        else:
            min_value = validate.float_answer('Digite a quantidade mínima: ')
            print()
            max_value = validate.float_answer('Digite a quantidade máxima: ')
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
