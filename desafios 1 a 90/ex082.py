numbers = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um número: '))
    numbers.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resposta = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resposta not in 'SN':
        resposta = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'A lista completa é : {numbers}')
print(f'A lista dos pares é: {pares}')
print(f'A lista dos ímpares é: {impares}')
#solução do professor abaixo
'''for i, v in enumerate(numbers):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)'''
