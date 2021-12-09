cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'azul':'\033[34m'}
num = int(input('Digite um número inteiro: '))
print('[{}1{}] converter para BINÁRIO'.format(cores['amarelo'], cores['limpa']))
print('[{}2{}] converter para OCTAL'.format(cores['amarelo'], cores['limpa']))
print('[{}3{}] converter para HEXADECIMAL'.format(cores['amarelo'], cores['limpa']))
choice = int(input('Sua escolha: '))
if choice == 1:
    print('O número {} em binário é: {}'.format(num, bin(num)[2:]))
elif choice == 2:
    print('O número {} em OCTAL é: {}'.format(num, oct(num)[2:]))
elif choice ==3:
    print('O número {} em HEXADECIMAL é: {}'.format(num, hex(num)[2:]))
else:
    print('{}Eu sou uma piada por acaso?{}'.format(cores['azul'], cores['limpa']))