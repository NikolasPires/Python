c = 1
while True:
    print('-'*30)
    n = int(input('Quer ver a tabuada de que número? '))
    print('-'*30)
    if n < 0:
        print('Programa encerrado...')
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
