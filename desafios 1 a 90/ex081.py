numbers = list()
while True:
    numbers.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resposta not in 'SN':
        resposta = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break
numbers.sort(reverse=True)
print('=' * 50)
print(f'Você digitou {len(numbers)} elementos')
print(f'Os valores decrescentes são {numbers}')
if 5 in numbers:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista')
