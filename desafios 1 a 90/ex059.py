from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
option = 0
while option != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    option = int(input('Qual é a sua opção? '))
    if option == 1:
        print('{} + {} = {}'.format(v1, v2, v1 + v2))
    elif option == 2:
        print('{} x {} = {}'.format(v1, v2, v1 * v2))
    elif option == 3:
        if v1 != v2:
            if v2 > v1:
                maior = v2
                menor = v1
            else:
                maior = v1
                menor = v2
            print(' {} > {}'.format(maior, menor))
        else:
            print('{} = {}'.format(v1, v2))
    elif option == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif option == 5:
        sleep(2)
        print('Saindo...')
    else:
        print('Opção inválida')
    sleep(2)
    print('=-='* 10)

