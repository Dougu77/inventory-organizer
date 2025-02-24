import pandas as pd
from utils import validate
from utils import get_data

def start() -> None:
    try:
        print('-' * 109)
        print(f'{"-" * 50} Estoque {"-" * 50}')
        print('-' * 109)
        print('\n- Esse programa ajuda na organização do estoque da loja.')
        print('- Visualize e edite os dados como desejar.')
        print('- Digite somente o número da opção que desejar.\n')
    except:
        error()

def table_not_found() -> None:
    print('A tabela não foi encontrada.\n')

def choice_crud() -> int:
    try:
        print('O que deseja fazer?\n')
        print('[ 1 ] Ver dados')
        print('[ 2 ] Adicionar produto')
        print('[ 3 ] Modificar produto')
        print('[ 4 ] Deletar produto')
        print('[ 5 ] Sair do programa\n')
        choice = validate.choice_number(5)
        print()
        return choice
    except:
        error()
        return 5

def error() -> None:
    print('Algo deu errado.\n')

def save_modifications(table:pd.DataFrame) -> None:
    try:
        table.to_excel(get_data.excel_path(), index=False)
        print('O arquivo Excel foi atualizado com sucesso!\n')
    except:
        print('O arquivo Excel não foi atualizado.\n')

def close() -> None:
    try:
        input('Digite ENTER para finalizar o programa...')
    except:
        error()
