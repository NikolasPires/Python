def maior(*num):
    maiore = max(num)
    print('-=' * 30)
    print('Analisando os dados passados...')
    for n in num:
        print(n, end=' ')
    print(f'Foram informados {len(num)} ao todo.')
    print(f'O maior valor foi {maiore}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
