p = float(input('Digite o seu peso em (kg): '))
h = float(input('Digite a sua altuma em (m): '))
IMC = p / (h**2)
print('Seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está ABAIXO DO PESO')
elif IMC < 25:
    print('Você está no PESO IDEAL')
elif IMC < 30:
    print('Você tem SOBREPESO')
elif IMC < 40:
    print('Você está na OBESIDADE')
else:
    print('Você está na OBESIDADE MÓRBIDA')