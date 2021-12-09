nome = 'Nikolas'
cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'azul':'\033[34m'}
print('Salve {}{}{}, seja muito bem-vindo'.format('\033[1:36m', nome, '\033[m'))
print('PARABÉNS!!! {}{}{} VOCÊ TIROU NOTA MIL NA REDAÇÂO'.format(cores['azul'], nome, cores['limpa']))
