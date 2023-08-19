'''3. Напишите декоратор debug, который при каждом вызове декорируемой функции выводит её имя (вместе со всеми
 передаваемыми аргументами), а затем — какое значение она возвращает. После этого выводится результат её выполнения.'''

def print_name(func):
    def f(*args, **kwargs):
        print(f'название функции {func.__name__}')
        if args:
            print(f'её  позиционные аргументы{[i for i in {*args} if i is not None]}')
            if kwargs:
                print(f'её именованные аргументы{[f"{i} - {j}" for i,j in kwargs.items()]}')
        else:
            print('Аргументов нет')
        print(f'что она возвращает - {func(*args, **kwargs)}')
        print(func(*args,**kwargs))
        return func
    return f

@print_name
def summ(a, b):
    return a+b

summ(2,3)

@print_name
def smpl():
    return 1-1
smpl()
