matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            spar += matrix[l][c]
        if c == 2:
            scol += matrix[l][c]
    print()
for c in range(0, 3):
    if c == 0:
        mai = matrix[1][c]
    elif matrix[1][c] > mai:
        mai = matrix[1][c]
print('-='*30)
print(f'A soma dos números pares é {spar}')
print(f'A soma dos números da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é {mai}')


