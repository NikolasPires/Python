sex = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sex not in 'MmFf':
    sex = str(input('Digita correctamente, por favor: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sex))
