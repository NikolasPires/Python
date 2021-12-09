values = list()
maior = menor = 0
for c in range(0, 5):
    values.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = values[c]
    else:
        if values[c] > maior:
            maior = values[c]
        if values[c] < menor:
            menor = values[c]
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(values):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for pos, n in enumerate(values):
    if n == menor:
        print(f'{pos}...', end='')
