viagem = float(input('Qual foi a  distância da viagem em Km/h? '))
preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('Você pagará um total de R${}'.format(preço))