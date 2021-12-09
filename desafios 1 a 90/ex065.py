s = cont = n = maior = menor = 0
resposta = 'Ss'
while resposta in 'Ss':
    cont += 1
    n = int(input('Digite um número: '))
    s += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S/N] ')).strip()[0]
print('Você digitou {} números e a média foi {:.2f}'.format(cont, s / cont))
print('O maior número foi {} e o menor {}'.format(maior, menor))
