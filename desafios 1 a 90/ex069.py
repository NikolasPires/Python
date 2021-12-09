maior = homens = garotas = 0
while True:
    print('='*20)
    print('CADASTRE UMA PESSOA')
    print('=' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip()[0]
    print('=' * 20)
    continuar = str(input('Quer continuar? [S/N] ')).strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] '))
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade <= 20:
        garotas += 1
    if continuar in 'Nn':
        print(f'Neste grupo há {maior} pessoas maiores de idade, \n{homens} homens e '
              f'{garotas} mulheres com menos de 20 anos')
        break
