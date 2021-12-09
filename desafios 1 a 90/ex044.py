print('{::^40}'.format('\033[33mLOJAS PIRES\033[m'))
price = float(input('Preço do produto: R$'))
print('\033[31mFORMAS DE PAGAMENTO\033[m')
print('\033[33m[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão\033[m')
pay = int(input('Digite um número: '))
if pay == 1:
    print('Sua compra à vista sairá com 10% de desconto \nO o valor é R${:.2f}'.format(price - price * 0.1))
elif pay == 2:
    print('Sua compra à vista no cartão sairá com 5% de desconto \nO valor é de R${:.2f}'.format(price - price * 0.05))
elif pay == 3:
    print('Sua compra foi parcelada em 2x no cartão,'
          ' cada parcela de R${}\n O valor é de R${:.2f}'.format(price / 2,price))
elif pay == 4:
    parcelas = int(input('Quantas parcelas?: '))
    juros = price + (price * 20/100)
    print('\033[34mSua compra  em 3x ou mais no cartão sairá com 20% de juros'
          '\n{}x de R${}\033[m '
          '\nO valor é total de \033[32mR${:.2f}'.format(parcelas, juros / parcelas, juros))
else:
    print('\033[31mTÁ ACHANDO QUE AQUI É O CIRCO?')

