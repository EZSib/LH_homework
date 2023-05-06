# Словарь с методами стандартных библиотек
# from pprint import pprint as pp
# pp(return_list, indent=2, width=140, compact=False, sort_dicts=True, underscore_numbers=True)
dct_Tkr = {
    'Tkinter': 'Модуль для создания графических приложений',
    'Tk –главное родительское окно приложения': 'Виджеты',
    'Toplevel–дочернее окно приложения': 'Виджеты',
    'Label–ярлык, отображаемый текст и изображения': 'Виджеты',
    '•anchor Label': 'устанавливает позиционирование текста',
    '•bg/background Label': 'фоновый цвет',
    '•bitmap Label': 'ссылка на изображение, которое отображается на метке',
    '•bd Label': 'толщина границы метки',
    '•fg/foreground Label': 'цвет текста',
    '•font Label': 'шрифт текста, например, font="Arial 14" -шрифт Arial высотой 14px',
    '•height Label': 'высота элемента',
    '•cursor Label': 'курсор указателя мыши при наведении на метку',
    '•image Label': 'ссылка на изображение, которое отображается на метке',
    '•justify Label': 'устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER -по центру, RIGHT -по правому краю',
    '•padx Label': 'отступ от границ элемента до его текста справа и слева',
    '•pady Label': 'отступ от границ элемента до его текста сверху и снизу',
    '•relief Label': 'определяет тип границы, по умолчанию значение FLAT',
    '•text Label': 'устанавливает текст метки',
    '•textvariable Label': 'устанавливает привязку к элементу StringVar ',
    '•underline Label': 'указывает на номер символа в тексте кнопки, который подчеркивается. По умолчанию значение -1, то есть никакой символ не подчеркивается',
    '•width Label': 'ширина элемента',
    '•wraplength Label': 'при положительном значении строки текста будут переносится для вмещения в пространство элемента',
    'Entry–текстовое поле ввода информации': 'Виджеты',
    '•bg Entry': 'фоновый цвет',
    '•cursor Entry': 'курсор указателя мыши при наведении на текстовое поле',
    '•fg Entry': 'цвет текста',
    '•font Entry': 'шрифт текста',
    '•justify Entry': 'устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER -по центру, RIGHT -по правому краю',
    '•relief Entry': 'определяет тип границы, по умолчанию значение FLAT ',
    '•selectbackground Entry': 'фоновый цвет выделенного куска текста',
    '•selectforeground Entry': 'цвет выделенного текста',
    '•show Entry': 'задает маску для вводимых символов',
    '•state Entry': 'состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED ',
    '•textvariable Entry': 'устанавливает привязку к элементу StringVar',
    '•width Entry': 'ширина элемента',
    '•bd Entry': 'толщина границы',
    'Button–кнопка': 'Виджеты',
    '•activebackground Button': 'цвет кнопки, когда она находится в нажатом состоянии',
    '•activeforeground Button': ' цвет текста кнопки, когда она в нажатом состоянии',
    '•bd Button': 'толщина границы (по умолчанию 2)',
    '•bg/background Button': 'фоновый цвет кнопки',
    '•fg/foreground Button': 'цвет текста кнопки',
    '•font Button': 'шрифт текста, например, font="Arial 14" -шрифт Arial высотой 14px, или font=("Verdana", 13, "bold") -шрифт Verdana высотой 13px с выделением жирным',
    '•height Button': 'высота кнопки',
    '•highlightcolor Button': 'цвет кнопки, когда она в фокусе',
    '•image Button': 'изображение на кнопке',
    '•justify Button': 'устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER -по центру, RIGHT -по правому краю',
    '•padx Button': 'отступ от границ кнопки до ее текста справа и слева',
    '•pady Button': 'отступ от границ кнопки до ее текста сверху и снизу',
    '•relief Button': 'определяет тип границы, может принимать значения SUNKEN, RAISED, GROOVE, RIDGE',
    '•state Button': 'устанавливает состояние кнопки, может принимать значения DISABLED, ACTIVE, NORMAL (по умолчанию)',
    '•text Button': 'устанавливает текст кнопки',
    '•textvariable Button': 'устанавливает привязку к элементу StringVar',
    '•underline Button': 'указывает на номер символа в тексте кнопки, который подчеркивается. По умолчанию значение -1, то есть никакой символ не подчеркивается',
    '•width Button': 'ширина кнопки',
    '•wraplength Button': 'при положительном значении строки текста будут переносится для вмещения в пространство кнопки',
    'Виджеты располагаются на экране с помощью упаковщиков':
        'Упаковщик .place() позволяет разместить виджет с помощью координат x, yНапример, btnOK.place(x = 20, y = 100)',
}


def search_in(string, dct=dct_Tkr):
    '''Функция поиска совпадений по подстроке, можно писать часть названия метода/функции
    или слово/часть слова из описания этой функции/метода'''
    Tkr_dok = {'В ключе указан Виджет к которому относится метод': '(последнее слово)'}
    return_list = []
    if dct == dct_Tkr:
        return_list.append(Tkr_dok)
    for name, info in dct.items():
        if string.lower() in name.lower() or string.lower() in info.lower():
            return_list.append({name: info})
    print('*' * 156)
    for i in return_list:
        print(*i)
        print(*(i.values()), end='\n' + 156 * '-' + '\n')

