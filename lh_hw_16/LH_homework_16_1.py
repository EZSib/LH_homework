'''1. Написать программы, которые продемонстрированы в видеоуроке.'''

class SmplItertor():

    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __next__(self):
        if self.limit >self.count:
            self.count += 1
            return self.count
        else:
            StopIteration

def smpl_gen(obj):
    while obj>0:
        obj -= 1
        yield obj

lst = smpl_gen(3)
print(next(lst))
print(next(lst))
print(next(lst))

print(list((x+1)*5 for x in range(1,55,5)))

