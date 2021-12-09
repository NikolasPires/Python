print('-'*40)
print('{:^40}'.format('BANCO BRILES'))
print('-'*40)
cedula = 50
totalced = somador = 0
saque = int(input('Quanto queres sacar? R$'))
total = saque
while True:
    if total > somador:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${cedula} ')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if somador == total:
            break
