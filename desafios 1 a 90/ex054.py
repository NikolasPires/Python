from datetime import date
maiores = 0
menores = 0
atual = date.today().year
for c in range(1, 8):
    ano_de_nascimento = int(input('Em que ano nasceu a {}ª pessoa? '.format(c)))
    if atual - ano_de_nascimento >= 21:
        maiores += 1
    else:
        menores += 1
print('Neste grupo há {} maiores de idade e {} menores de idade'.format(maiores, menores))
