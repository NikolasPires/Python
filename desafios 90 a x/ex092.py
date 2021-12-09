from _datetime import datetime
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
pessoa['Ano de nascimento'] = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.now().year - pessoa['Ano de nascimento']
pessoa['ctps'] = int(input('Carteira de Trabalho (0 se não a tem): '))
if pessoa['ctps'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = int(input('Salário: '))
    pessoa['Aposentadoria'] = (pessoa['Ano de contratação'] - pessoa['Ano de nascimento']) + 35
print('-='*30)
for k, v in pessoa.items():
    print(f'  - {k} tem valor {v}')
