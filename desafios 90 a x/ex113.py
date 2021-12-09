def leiaint(frase):
    while True:
        try:
            n = int(input(frase))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um NÚMERO INTEIRO válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiafloat(frase):
    while True:
        try:
            n = float(input(frase))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um NÚMERO REAL válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n

num = leiaint('Digite um número inteiro: ')
real = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num}')
print(f'O número real digitado foi {real}')
