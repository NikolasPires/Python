num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
       'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
       n = int(input('Digite um número entre 0 e 20: '))
       while n > 20 or n < 0:
              n = int(input('Digite um número entre 0 e 20: '))
       print(f'Tu digitaste o número \033[33m{num[n]}\033[m')
       continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
       if continuar not in 'SN':
              print('Tente novamente...')
              continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
       if continuar == 'N':
              break