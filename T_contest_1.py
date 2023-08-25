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

# n, k = map(int, (input().split()))
# list_n = list(map(int, (input().split())))
# list_n_str = list(map(str,list_n))
# sum_staart = sum(list_n)
# total = 0
# not_9 = abs([i for i in list_n_str if i.isdigit()].count('9')-len([i for i in list_n_str if i.isdigit()]))
# rep = 0
# if k >= n:
#     total = sum(map(int, (map(lambda x: '9' * len(x), list_n_str)))) - sum_staart
# else:
#     three = sorted(list(filter(lambda x: len(x)==3, list_n_str)))
#     sec_three = list(map(lambda x: str(x)[1:], three))
#     twoo =  sorted(list(filter(lambda x: len(x)==2, list_n_str)) + sec_three)
#     sec_two = list(map(lambda x: str(x)[1:], twoo))
#     onee =  sorted(list(filter(lambda x: len(x)==1, list_n_str)) + sec_two)
#     while k > 0 or rep == not_9 or any(three + twoo + onee) == False:
#         if three:
#             if int(three[0][0]) != 9:
#                 total += (9 - int(three[0][0])) * 100
#                 k -=1
#                 rep +=1
#                 del three[0]
#             else:
#                 three.clear()
#         elif twoo:
#             if int(twoo[0][0]) != 9:
#                 total += (9 - int(twoo[0][0])) * 10
#                 k -=1
#                 rep +=1
#                 del twoo[0]
#             else:
#                 twoo.clear()
#         elif onee:
#             if int(onee[0]) != 9:
#                 total += (9 - int(onee[0]))
#                 k -=1
#                 rep +=1
#                 del onee[0]
#             else:
#                 onee.clear()
# print(total)

'''задача где надо найти все числа с одинаковыми цифрами в промежутке'''
# a, b = map(int, (input().split()))
# cnt = 0
#
# for i in range(a,b+1):
#     if str(i).count(str(i)[0]) == len(str(i)):
#         cnt+=1

n = int(input())
rank = list(map(int, input().split()))
result = '-1-1'
odd = list(map(lambda x: x % 2 ==1, rank))
even = list(map(lambda x: x % 2 ==0, rank))
if sum(odd) < sum(even)   or  (all(odd[::2]) and all(even[1::2])) or \
        (''.join(list(map(int, odd))).count('00') > 1 or ''.join(list(map(int, odd))).count('11') > 1):
    print(result)
else:
    swap =

