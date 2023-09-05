def sale():
    shopping_list = []
    print('welcome'.upper())
    stdinp = input('Введите наименование товара (завершить - "стоп")\n')
    while stdinp != 'стоп':
        shopping_list.append(stdinp)
        stdinp = input('Введите наименование товара (завершить - "стоп")\n')
    print(f'===Корзина Товаров===\n', *shopping_list, sep='\n')
    resale = int(input('Хотите собрать новую корзину?\n1- ДА\n2- нет\n'))
    if resale == 1:
        sale()
    else:
        print('Have a nice day')


sale()
