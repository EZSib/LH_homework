import math

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

quantity_leave, levels, first_leave = (list(map(int, (input().split()))) for _ in range(3))
first_leave_lvl = levels[first_leave[0]-1]
if quantity_leave[1] >= sum((levels[:first_leave[0]-1])):
    print(levels[-1]-levels[0])
