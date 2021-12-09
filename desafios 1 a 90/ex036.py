imo = int(input('Qual é o valor do imóvel? R$'))
sail = int(input('Quanto você ganha por mês? R$'))
fin = int(input('em quantos anos você deseja financiar? '))
prest = imo / (fin *12)
print('\033[33m=\033[m' * 55)
print('A prestação do seu imóvel será de R${:.2f} em {} anos'.format(prest, fin))
print('\033[33m=\033[m' * 55)
if prest >= sail *0.30:
    print('{}O BANCO DECIDIU NEGAR SUA REQUISIÇÃO DE FINANCIAMENTO'
          '\nPOIS A PRESTAÇÂO DE R${:.2f} EXCEDEU 30% DO SALÁRIO'.format('\033[31m', prest))
else:
    print('SUA REQUISIÇÃO FOI AVALIADA \n\033[1:32mE O EMPRÉSTIMO FOI APROVADO!')