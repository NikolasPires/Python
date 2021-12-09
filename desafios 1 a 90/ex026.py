nome = str(input('Digite um nome: ')).lower().strip()
print('A letra A aparece {} vezes na frase'.format(nome.count('a')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('a') + 1))
print('A Letra A aparece por sua última vez na posição {}'.format(nome.rfind('a') + 1))
