def choice_number(max_number:int) -> int:
    while True:
        number = input('Opção: ').strip()
        try:
            if 1 <= int(number) <= max_number:
                break
            else:
                print(f'Digite um número entre 1 e {max_number}.')
        except:
            print('Digite um valor numérico.')
    return int(number)

def string_answer(question:str) -> str:
    while True:
        answer = input(question).strip()
        if len(answer) > 0:
            break
        else:
            print('Digite alguma coisa.')
    return answer

def float_answer(question:str) -> float:
    while True:
        answer = input(question).strip()
        try:
            if float(answer):
                break
        except:
            print('Digite um valor numérico.')
    return float(answer)
