def fatorial(num, show=False):
    """"
    -> Calcula o factorial de um número.
    :param num: Número cujo fatorial será calculado.
    :param show: (Opcional) Mostra o processo da operação.
    :return: Resultado da operação do fatorial num.
    """
    f = 1
    print('~'*30)
    for c in range(num, 0, -1):
        f *= c
        if show is True:
            if c > 1:
                print(c, end=' x ')
            if c == 1:
                print(f'{c} = ', end='')
    return f

#print(fatorial(5, True))
help(fatorial)
