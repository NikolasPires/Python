from datetime import date
nome = str(input('Digite o seu nome: '))
nasc = int(input('Digite ano em que você nasceu: '))
atual = date.today().year
age = atual - nasc
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarela':'\033[33m',
         'vermelha':'\033[31m'}
print('Olá {}{}{}.\nDe acordo com a sua idade de {} anos'
      '\nsua categoria é:'.format(cores['azul'], nome, cores['limpa'], age))
if age <= 9:
    print('MIRIM')
elif age <= 14:
    print('{}INFANTIL'.format(cores['amarela']))
elif age <= 19:
    print('{}JÚNIOR'.format(cores['amarela']))
elif age <= 25:
    print('{}SÊNIOR'.format(cores['amarela']))
else:
    print('{}MASTER'.format(cores['vermelha']))
