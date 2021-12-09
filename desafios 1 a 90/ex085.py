numbers = [[], []]
dados = list()
for c in range(0, 7):
    dados.append(int(input('Digite um valor: ')))
    numbers.append(dados[:])
    dados.clear()
for n in numbers:
    if n >= numbers[2]:
        if n[0] % 2 == 0:
            numbers[0].append(n[0])
        if n[0] % 2 == 1:
            numbers[1].append(n[0])
del numbers[2:]
numbers[0].sort()
numbers[1].sort()
print('='*30)
print(f'Os números pares digitados são: {numbers[0]}')
print(f'Os nuúmeros ímpares digitados são: {numbers[1]}')
