import sqlite3
def sale():
    conn = sqlite3.connect('data_shopping.db')
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    cur.execute('''CREATE TABLE  IF NOT EXISTS shopping_lists(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        shopping_cart VARCHAR(64) NOT NULL,
        product VARCHAR(64)
        )''')
    print('welcome'.upper())
    cart_name = input('Введите название вашей корзины покупок\n')
    stdinp = input('Введите наименование товара (завершить - "стоп")\n')
    while stdinp != 'стоп':
        params = (cart_name, stdinp)
        cur.execute('INSERT INTO shopping_lists VALUES (NULL, ?, ?)', params)
        conn.commit()
        print(f'{stdinp} добавлен в корзину {cart_name}')
        stdinp = input('Введите наименование товара (завершить - "стоп")\n')

    print(f'===Корзины Товаров===', *set(cur.execute('SELECT shopping_cart FROM shopping_lists')), sep='\n')
    resale = input('1- Собрать новую корзину\nНазвание корзины- просмотреть содержимое корзины\nстоп - выйти \n')
    while resale != 'стоп':
        if resale == '1':
            sale()
        else:
            cur.execute('SELECT product FROM shopping_lists WHERE shopping_cart = ?', (resale,))
            [print (f'{nmb} - {prod}') for nmb, prod in enumerate(cur.fetchall(), 1)]
            print(f'===Корзины Товаров===', *set(cur.execute('SELECT shopping_cart FROM shopping_lists')), sep='\n')
            resale = input('1- Собрать новую корзину\nНазвание корзины- просмотреть содержимое корзины\nстоп - выйти\n')
    print('Have a nice day')
    conn.close()
    exit()
sale()
