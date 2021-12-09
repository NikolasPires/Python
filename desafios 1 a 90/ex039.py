from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
sing = 18 - idade
print('Quem nasceu em {} tem {} anos  em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar o mais breve possível!')
elif sing == 1:
    print('Você deve se alistar daqui há {} ano'.format(18 - idade))
elif idade < 18:
    print('Você deve se alistar daqui há {} anos'.format(18 - idade))
else:
    print('Você já devería ter se alistado há {} anos'.format(idade - 18))


