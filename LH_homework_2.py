# Задача  номер 1.
# Как вариант:
# from sys import stdin
# total = 0
# for i in stdin:
#     total += int(i)
#     if int(i) == 0:
#         print(total)
#         break

total = 0
inp = int(input())
while inp != 0:
    total += inp
    inp = int(input())
print(total)

# Задача номер 2

fruits = ['яблоки', 'апельсины', 'бананы'] + ['манго', 'виноград']
del fruits[fruits.index('апельсины')]
print(fruits, len(fruits), sep='\n')
