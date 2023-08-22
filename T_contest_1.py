import math
from random import shuffle
# print(len([i for i in list(range(100,1000)) if (int(str(i)[0]))+int(str(i)[1])+int(str(i)[2]) == i/19]))
# print(8*math.sqrt(7))
'''Вводится 4 целых положительных числа ABCD(1≤A,B,C,D≤100)
A,B,C,D(1≤A,B,C,D≤100) — стоимость тарифа Кости, размер тарифа Кости, стоимость каждого лишнего мегабайта, размер интернет-трафика
Кости в следующем месяце. Числа во входном файле разделены пробелами'''

# A,B,C,D = map(int, (input().split()))
#
# if D <= B:
#     print(A)
# else:
#     print(f'{A + (D-B) * C}')

# '''задача с рулетом'''
#
# n = int(input())
# start = 1
# slice = dict()
# slice[(1,)] = 0
# for i in range(1,35):
#   slice[(range(2**i,2**(i-1),-1))] = start
#   start += 1
# for k, v in slice.items():
#     if n in k:
#         print(v)

'''задача с лестницами '''

# quantity_leave, levels, first_leave = (list(map(int, (input().split()))) for _ in range(3))
#
# first_leave_lvl = levels[first_leave[0]-1]
#
# if quantity_leave[1] >= (first_leave_lvl - levels[0] or levels[-1] - first_leave_lvl) or first_leave[0] == 1 or first_leave[0] == len(levels):
#     print(levels[-1]-levels[0])
# else:
#     print(min([first_leave_lvl - levels[0] + levels[-1] - 1, levels[-1] - first_leave_lvl  + (levels[-1]-levels[0])]))

'''Задача с листочком на котором написаны числа, их надо переписать чтоб получить большую сумму'''

n, k = map(int, (input().split()))
list_n = list(map(int, (input().split())))
list_n_str = list(map(str,list_n))
sum_staart = sum(list_n)
total = 0
if k >= n:
    print(sum(map(int, (map(lambda x: '9' * len(x), list_n_str)))) - sum_staart)
else:
    while k>0:
        th_rd = list(filter(lambda x: len(x)==3), list_n_str)
# print(n,k,list_n,sum_staart)
# print(list_n_str)
# print(min('987','986'))
print(sorted(['12','9','111', '1000']))