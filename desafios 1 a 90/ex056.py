midade = 0
maior = 0
name = 0
mulieres = 0
for c in range(1, 5):
    print('-' * 5, '{}ª PESSOA'.format(c), '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: '))
    midade += idade
    if c == 1 and sexo in 'Mm':
        maior = idade
        name = nome
    if sexo in 'Mm' and idade > maior:
            maior = idade
            name = nome
    if sexo in 'Ff' and idade < 20:
        mulieres += 1
print('A média das idades é {}'.format(midade/4))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, name))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulieres))
print('-'*21)
