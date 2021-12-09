from time import sleep
vel = int(input('Qual é a velocidade do seu carro em km/h? '))
multa = vel - 80
if multa >= 1:
    sleep(1)
    print('PRESTE MAIS ATENÇÃO À SUA VELOCIDADE \nVocê foi multado em R${}'.format(multa * 7))
else:
    print('Muito bem, sua velocidade está sob controle \n Pode seguir em frente')
