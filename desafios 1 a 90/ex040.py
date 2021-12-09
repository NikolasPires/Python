n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
print('As notas foram {:.1f} e {:.1f}. A média é {}'.format(n1, n2, média))
if média < 5:
    print('{}REPROVADO!{}'.format('\033[31m','\033[m'))
elif média >= 7:
    print('{}APROVADO, PARABÉNS!{}'.format('\033[32m', '\033[m'))
elif 5 <= média < 7:
    print('{}RECUPERAÇÃO!{}'.format('\033[33m','\033[m'))