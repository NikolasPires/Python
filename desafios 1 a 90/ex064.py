n = cont = s = 0
n = int(input('Digite um número [999 para parar] '))
while n != 999:
    s += n
    cont += 1
    n = int(input('Digite um número [999 para parar] '))
print('A somatória de todos os {} números é {}'.format(cont, s))
