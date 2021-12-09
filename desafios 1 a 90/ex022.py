#Analisador de textos
p = str(input('Digite seu nome inteiro: ')).strip()
print (p.upper())
print (p.lower())
print ('O nome inteiro tem {} letras'.format(len(p) - p.count(' ')))
f = p.split()
print('O primeiro nome tem {} letras'.format(len(f[0])))
