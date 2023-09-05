'''2. Напишите класс-итератор, объекты которого генерируют случайные числа в количестве и в диапазоне, которые передаются в конструктор.'''
from random import randint

class RandomIterator():
    def __init__(self, quantity, rng):
        self.quantity = quantity
        self.rng = rng
        self.cnt = 0
    def __next__(self):
        if  self.quantity > self.cnt:
            self.cnt += 1
            return randint(min(self.rng), max(self.rng))
        else:
            raise StopIteration

rnd_iter = RandomIterator(5, (1,9))
print(next(rnd_iter))
print(next(rnd_iter))
print(next(rnd_iter))
print(next(rnd_iter))
print(next(rnd_iter))
print(next(rnd_iter))
