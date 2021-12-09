def voting(born):
    from datetime import date
    actual = date.today().year
    age = actual - born
    if age > 65 or 16 <= age < 18:
        return f'Com {age} anos: VOTO OPCIONAL'
    elif 65 > age >= 18:
        return f'Com {age} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {age} anos: NÃO VOTA'


year = voting(int(input('Em que ano você nasceu? ')))
print(year)
