from random import randint
computador = randint(0, 10)
tentativas = 0
resultado = False
while resultado == False:
    jogador = int(input('Qual é o seu palpite? '))
    if jogador == computador:
        resultado = True
    else:   
        if jogador > computador:
            print('Menos... tente mais uma vez')
        elif jogador < computador:
            print('Mais.. tente mais uma vez')
    tentativas += 1
print('Acertou com {} tentativas. Parabéns'.format(tentativas))
