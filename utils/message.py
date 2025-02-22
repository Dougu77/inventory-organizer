from utils import validate

def start() -> None:
    print('-' * 109)
    print(f'{"-" * 50} Estoque {"-" * 50}')
    print('-' * 109)
    print('\n- Esse programa ajuda na organização do estoque da loja.')
    print('- Visualize os dados como desejar, e edite os dados como quiser.')
    print('- Digite somente o número da opção que desejar.\n')

def choice_crud() -> int:
    print('[ 1 ] Ver dados')
    print('[ 2 ] Adicionar produto')
    print('[ 3 ] Modificar produto')
    print('[ 4 ] Deletar produto')
    print('[ 5 ] Sair do programa\n')
    choice = validate.choice_number('Escolha uma opção: ', 5)
    print()
    return choice
