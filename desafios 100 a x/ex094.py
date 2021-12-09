pessoas = list()
s = 0
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Erro!!  Sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(pessoa)
    if resposta in 'N':
        break
for p in pessoas:
    s += p['idade']
media = s/len(pessoas)
print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A média das idades é {media:.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'F':
        print(p['nome'], end=' ')
print()
print('D) Lista das pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<< FINALIZADO >>')
