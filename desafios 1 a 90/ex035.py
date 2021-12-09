print('='*16)
print(' TESTE DE FORMAÇÂO DE UM TRIÂNGULO')
print('='*16)
r1 = float(input('Primeiro segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos de reta {}, {}, e {} PODEM FORMAR UM TRIÂNGULO'.format(r1, r2, r3))
else:
    print('os segmentos de reta {}, {}, e {} NÂO PODEM FORMAR UM TRIÂNGULO'.format(r1, r2, r3))