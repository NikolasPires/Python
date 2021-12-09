nome = str(input('Qual é o seu nome: '))
if nome == 'Nikolas':
    print('Que nome {}bonito{}!'.format('\033[1:36m', '\033[m'))
elif nome == 'Maria' or nome == 'Pedro' or nome == 'João':
    print('É um nome bastante tradicional!')
elif nome in 'Adalberto Bartolomeu Baltazar Evandro Creuza':
    print('Que nome mais {}estranho{}'.format('\033[:033m', '\033[m'))
else:
    print('Seu nome é muito normal')
print('Tenha um bom dia, {}!'.format(nome))
