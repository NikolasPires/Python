numbers = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Os valores digitados foram: {numbers}')
print(f'O valor 9 apareceu {numbers.count(9)} vezes')
if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3) + 1}ª posição ')
else:
    print('Não há valor nenhum 3')

print('Os valoes pares foram: ', end='')
for c in numbers:
    if c % 2 == 0:
        print(c, end=' ')
