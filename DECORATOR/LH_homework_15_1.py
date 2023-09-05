'''1. Напишите две функции создания списка из четных чисел от 0 до N (N – аргумент функции):
[0, 2, 4, …, N] с помощью метода append и с помощью инструмента list comprehensions (генератор списков).
 Через декоратор определите время работы этих функций.'''
# '====================================================================================================================='
from datetime import datetime


def time_dec(func):
    def action(x):
        now = datetime.now()
        func(x)
        return datetime.now() - now

    return action


@time_dec
def func_even_append(n):
    list_even = []
    for i in range(0, n):
        if i % 2 == 0:
            list_even.append(i)
    return list_even


@time_dec
def func_even_comprehensions(n):
    return [i for i in range(0, n) if i % 2 == 0]


print(func_even_append(1000000))
print(func_even_comprehensions(1000000))
