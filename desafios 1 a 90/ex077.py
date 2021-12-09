words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
         'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
         'PROGRAMADOR', 'FUTURO')
print(words[0].find('E'))
for c in words:
    print('\nNa palavra {} temos '.format(c.upper()), end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
