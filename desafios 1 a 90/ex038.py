n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    maior = n1
    menor = n2
    print('{} > {}'.format(maior, menor))
elif n2 > n1:
    maior = n2
    menor = n1
    print('{} > {}'.format(maior, menor))
else:
    print('{} = {}'.format(n1, n2))
