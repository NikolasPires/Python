#Cálculo da hipotenusa
'''from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = sqrt(co ** 2 + ca ** 2)
print('A hipotenusa medirá: {:.2f}'.format(h))'''

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa medirá: {:.2f}'.format(hi))

