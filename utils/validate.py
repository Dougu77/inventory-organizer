def string_answer(question:str, number_pontuation:bool=False) -> str:
    while True:
        answer = input(question).strip()
        if len(answer) > 0:
            if number_pontuation:
                answer = answer.replace(',', '.')
            break
        else:
            print('Digite alguma coisa.')
    return answer

def float_answer(question:str) -> float:
    while True:
        answer = string_answer(question, True)
        try:
            if float(answer):
                break
        except:
            print('Digite um valor numérico.')
    return float(answer)

def int_answer(question:str) -> int:
    while True:
        answer = string_answer(question, True)
        try:
            if int(answer):
                break
        except:
            print('Digite um valor numérico.')
    return int(answer)

def choice_number(max_number:int) -> int:
    question = 'Opção: '
    while True:
        number = int_answer(question)
        if 1 <= number <= max_number:
            break
        else:
            print(f'Digite um número entre 1 e {max_number}.')
    return int(number)

def min_price_value() -> float:
    question = 'Digite o preço mínimo: '
    while True:
        value = float_answer(question)
        if value <= 0:
            print('Digite um preço maior que zero.')
        else:
            break
    return value

def max_price_value(min_value:float) -> float:
    question = 'Digite o preço máximo: '
    while True:
        value = float_answer(question)
        if value < min_value:
            print('Digite um preço maior que o preço mínimo.')
        else:
            break
    return value

def min_quantity_value() -> int:
    question = 'Digite a quantidade mínima: '
    while True:
        value = int_answer(question)
        if value < 0:
            print('Digite uma quantidade maior ou igual a zero.')
        else:
            break
    return value

def max_quantity_value(min_value:int) -> int:
    question = 'Digite a quantidade máxima: '
    while True:
        value = int_answer(question)
        if value < min_value:
            print('Digite uma quantidade maior que a quantidade mínima.')
        else:
            break
    return value

def create_or_update_price() -> float:
    question = 'Digite o preço: '
    while True:
        price = float_answer(question)
        if price <= 0:
            print('Digite um preço maior que zero.')
        else:
            break
    return round(price, 2)

def create_or_update_quantity() -> int:
    question = 'Digite a quantidade: '
    while True:
        quantity = int_answer(question)
        if quantity < 0:
            print('Digite uma quantidade maior ou igual a zero.')
        else:
            break
    return quantity
