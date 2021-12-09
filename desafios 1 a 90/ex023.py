n = int(input('Digite um número: '))
'''resolvedor = str(n + 100000)
print(resolvedor)
print('Unidade: {}'.format((resolvedor[5])))
print('Dezena: {}'.format(resolvedor[4]))
print('Centena:{}'.format(resolvedor[3]))
print('Milhar: {}'.format(resolvedor[2]))'''
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
