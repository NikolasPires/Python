def notas(*lista, sit=False):
    """"
    -> Função que analisa as notas e a situação de vários alunos e mostra o resultado.
    :param lista: Notas dos alunos.
    :param sit: (Opcional) Mostra a situação do aluno referente à média de sua nota.
    :return: Retorna, em forma de dicionário, todas as informações acerca da nota do aluno.
    """
    tabela = dict()
    tabela['total'] = len(lista)
    tabela['maior'] = max(lista)
    tabela['menor'] = min(lista)
    tabela['média'] = sum(lista) / len(lista)
    if tabela['média'] >= 7:
        situacao = 'Boa'
    elif tabela['média'] <= 5:
        situacao = 'Ruim'
    else:
        situacao = 'Razoável'
    if sit:
        tabela['situação'] = situacao
    return tabela


resp = notas(2, 4, 6, 8, 10, sit=True)
print(resp)
