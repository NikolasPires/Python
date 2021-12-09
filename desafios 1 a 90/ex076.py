produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15, 'Estojo', 25,
            'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32,
            'Canetas', 22.3, 'Livro', 34.90)
cont = 0
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PRODUTOS'))
print('-'*40)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f'R${produtos[item]:>8.2f}')
print('-'*40)
