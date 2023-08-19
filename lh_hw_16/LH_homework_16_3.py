'''3.В предыдущем задании требовалось написать класс-итератор, объекты которого генерируют случайные числа в количестве
 и в диапазоне, которые передаются в конструктор.
Напишите выполняющую ту же задачу генераторную функцию. В качестве аргументов она должна принимать количество элементов и диапазон.'''

from random import randint

def RandomGenerator(quantity, rng):
        while  quantity > 0:
            quantity -= 1
            yield randint(min(rng), max(rng))
rnd_iter = RandomGenerator(5, (1,9))
print(next(rnd_iter))
print(next(rnd_iter))
print(next(rnd_iter))
print(next(rnd_iter))
print(next(rnd_iter))
print(next(rnd_iter))