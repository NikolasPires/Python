sal =  float(input('Digite o seu salário para calcular o aumento: R$'))
if sal >= 1250:
    aumento = sal + (sal * 0.10)
else:
    aumento = sal + (sal * 0.15)
print('Antes você ganhava R${} \nA partir de agora você ganhará R${}'.format(sal, aumento))