c =('\033[m',           #0 limpa
    '\033[0:39:42m',    #1 verde
    '\033[0:39:44m',    #2 azul
    '\033[0:30:107m'    #3 branco
    )


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')


def ajuda(msg):
    from time import sleep
    while True:
        print('\033[0:39:42m')
        titulo('SISTEMA DE AJUDA PyHelp', 1)
        print('\033[m')
        h = str(input(msg))
        if h.upper() in 'FIM':
            break
        sleep(1)
        titulo(f'Acessando manual do comando \'{h}\'', 2)
        sleep(1)
        print(c[3], end='')
        help(h)
        print(c[0])


ajuda('Função ou Biblioteca: ')
