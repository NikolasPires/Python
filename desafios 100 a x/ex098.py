from time import sleep
def contador(a, b, c):
    print('-=' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if b < a:
        c = -c
        b = b - 1
    else:
        b = b + 1
    for cont in range(a, b, c):
        print(cont, end=' ')
        sleep(0.5)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora és tu que decides o destino do contador!')
n1 = int(input('Começo: '))
n2 = int(input('Fim: '))
n3 = int(input('Passo: '))
contador(n1, n2, n3)
