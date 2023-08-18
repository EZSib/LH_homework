'''3. Напишите декоратор debug, который при каждом вызове декорируемой функции выводит её имя (вместе со всеми
 передаваемыми аргументами), а затем — какое значение она возвращает. После этого выводится результат её выполнения.'''

def print_name(func):
    def f(*args, **kwargs):
        print(f' название функции {func.__name__}')
        print(f' её аргуметы {[i for i in {*args, kwargs.items()} if i]}')
        print(f' что она возвращает {func(*args, **kwargs)}')
        return func
    return f

@print_name
def summ(a,b):
    return a+b

summ(2,3)