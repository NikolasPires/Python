#Analisador de palíndromo
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.split()
frase = ''.join(frase)
inverso = frase[::-1]
print('A frase é \033[33m{}\033[m e seu inverso \033[31m{}\033[m'.format(frase, inverso))
if frase == inverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
