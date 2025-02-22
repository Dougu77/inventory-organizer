import pandas as pd
from utils.enum import ColumnName
from utils import validate
from utils import get_data

def start() -> None:
    print('-' * 109)
    print(f'{"-" * 50} Estoque {"-" * 50}')
    print('-' * 109)
    print('\n- Esse programa ajuda na organização do estoque da loja.')
    print('- Visualize os dados como desejar, e edite os dados como quiser.')
    print('- Digite somente o número da opção que desejar.\n')

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

def read_table(table:pd.DataFrame) -> None:
    print(table)
    print()

def read_product(table:pd.DataFrame) -> None:
    item_name = validate.string_answer('Digite o nome do produto: ')
    print()
    item_data = get_data.specific_row(table, ColumnName.ITEM.value, item_name)
    if item_data.empty:
        print('A pesquisa não retornou resultados.')
    else:
        print(item_data)
    print()
