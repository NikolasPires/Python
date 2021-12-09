total = caro = barato = contador = 0
produtobarato = ''
print('='*20)
print('LOJAS INSETICIDA')
print('='*20)
while True:
    product = str(input('Nome do produto: '))
    price = float(input('Preço: R$'))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    contador += 1
    total += price
    if price >= 1000:
        caro += 1
    if contador == 1 or price < barato:
        barato = price
        produtobarato = product
    if continuar == 'N':
        print('{:-^40}'.format('FIM DO PROGRAMA'))
        print(f'O total gasto na compra foi de R${total:.2f}'
              f'\nHouveram {caro} produtos com mais de R$1000'
              f'\nO produto mais barato foi {produtobarato} custando R${barato:.2f}')
        break
