def choice_number(question:str, max_number:int) -> int:
    while True:
        number = input(question).strip()
        try:
            if 1 <= int(number) <= max_number:
                break
            else:
                print(f'Digite um número entre 1 e {max_number}.')
        except Exception:
            print('Digite um valor numérico.')
    return int(number)
