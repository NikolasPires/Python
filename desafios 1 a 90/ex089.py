
dados = list()
while True:
    aluno = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista = [n1, n2, media]
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta in 'N':
        break
print('-='*30)
print('No. NOME {:>15}'.format('MÉDIA'))
for i, c in enumerate(lista):
    print(f'{i}   {c[0]:<15}{c[3]}')
print('-'*20)
while True:
    pergunta = int(input('Quer mostrar a nota de qual aluno? (999 interrompe): '))
    if pergunta == 999:
        break
    print(f'Notas de {lista[pergunta][0]} são {lista[pergunta][1], lista[pergunta][2]}')
    print('-'*20)
print('Finalizando...')
print('<<< VOLTE SEMPRE >>>')
