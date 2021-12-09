pessoas = list()
dados = list()
cont = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
    cont += 1
for p in range(0, len(pessoas)):
    if p == 0:
        menor = maior = pessoas[0][1]
    if pessoas[p][1] >= maior:
        maior = pessoas[p][1]
    elif pessoas[p][1] < menor:
        menor = pessoas[p][1]
print('=-=' * 30)
print(f'Você cadastrou {cont} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi {menor}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
