numbers = list()
count = 0
while True:
    n = int(input('Digite um número: '))
    if n not in numbers:
        numbers.append(n)
    else:
        print('Valor Duplicado! Não adicionarei...')
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    count += 1
    if resposta in 'N':
        print(f'Você digitou os números: {sorted(numbers)}')
        break
