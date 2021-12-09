from  random import randint
computador = randint(1, 10)
vitórias = 0
print('=-='*10)
print('\033[33m{:^}\033[m'.format('VAMOS JOGAR PAR OU IMPAR'))
print('=-='*10)
while True:
    v = int(input('Digite um valor: '))
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print('---'*10)
    soma = v + computador
    if soma % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'
    print(f'Você jogou {v} e o computador jogou {computador}. \n{v} + {computador} = {soma} {resultado}')
    print('---'*10)
    if op in resultado[0]:
        print('Você \033[32mGanhou\033[m!')
        vitórias += 1
    else:
        print('Você \033[31mPerdeu\033[m')
        print('-=-'*10)
        print(f'GAME OVER! você ganhou {vitórias} vezes.')
        break
