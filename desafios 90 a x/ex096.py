def area(l , c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')


print('  Controle de terrenos')
print('-'*22)
l = int(input('Largura (m): '))
c = int(input('Comprimento (m): '))
area(l, c)
