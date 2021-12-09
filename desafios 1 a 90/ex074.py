from random import randint
num = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
maior = menor = 0
print(f'Os valores sorteados foram: ', end='')
for c in num:
    print(f'{c}', end=' ')
'''if c == num[0]:
        maior = c
        menor = c
    if c > maior:
        maior = c
    if c < menor:
        menor = c'''
#print(f'O maior é {maior} e o menor {menor}')
print(f'\nO maior valor sorteado foi {max(num)}'
      f'\nO menor valor sorteado foi {min(num)} ')