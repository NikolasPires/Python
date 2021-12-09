def leianum(frase):
    n = str(input(frase)).strip()
    while True:
        if n.isnumeric():
            break
        print('\033[31mErro! Digite um número inteiro válido\033[m')
        n = str(input(frase))
    return n


n = leianum('Digite um número: ')
print(f'Você digitou o número {n}')