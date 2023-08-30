import math
from random import shuffle
from decimal import Decimal as D
from decimal import getcontext

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

'''задача с перестановкой цифр'''
# n = int(input())
# rank = list(map(int, input().split()))
# result = -1,-1
# odd = list(map(lambda x: x % 2 ==1, rank))
# even = list(map(lambda x: x % 2 ==0, rank))
# one_zero = ''.join(list(map(str, (map(int, odd)))))
# if sum(odd) < sum(even)   or  (all(odd[::2]) and all(even[1::2])) or \
#         (one_zero.count('00') > 1 or one_zero.count('11') > 1):
#     print(*result)
# else:
#     try:
#         print(*(one_zero.find('00')+2, one_zero.find('00')+3))
#     except:
#         print(*(one_zero.find('11')+2, one_zero.find('11')+3))

'''тайный санта от 1 к 1 (уточнить детали непонятны выходные условия)'''

# n = int(input())
# rank = list(map(int, input().split()))
# if (len(rank) - len(set(rank)) != 1) or (rank[0] != rank[-1]) or (rank[0] != rank[-2]) or (rank[1] != rank[-1]):
#     print(*(-1, -1))


'''грязное дело в переговорке ( задача с масштабом и поиском точки соприкосновения)'''
# getcontext().prec = 5
# x, y = map(int, input().split())
# rect = list(map(float, input().split()))
# x0, y0, x1, y1 = (rect[0], rect[1]), (rect[2], rect[3]), (rect[4], rect[5]), (rect[6], rect[7])
# scale = D(x / abs(x0[0] - x1[0]))
# d1, d2, d3, d4 = D(0.1), D(0.01), D(0.001), D(0.0001)
#
# start, res = (0, 0), x0
# for i in range(max(x, y)):
#     if res != x0:
#         break

# def paper(A, main_rect=D(0), paper_rect=D(0)):
#     A = D(A)
#
#     # elif x0[0] > x1[0] and x0[1] > x1[1]:
#     f, s, res = main_rect, A, paper_rect
#     for i in range(x):
#         if res != 0:
#             break
#         if (f + i) == (s - i / scale) == (res + i):
#             res += i
#             return res
#         elif (s - i / scale) < (res + i):
#             f, s, res = (f + i - 1), (s - (i - 1) / scale), (res + i - 1)
#             for j in range(1, 10):
#                 if (f + D(f'0.{j}')) == (s - D(f'0.{j}') / scale) == (res + D(f'0.{j}')):
#                     res += D(f'0.{j}')
#                     return res
#                 elif (s - D(f'0.{j}') / scale) < (res + D(f'0.{j}')):
#                     f, s, res = (f + D(f'0.{j}') - d1), (s - (D(f'0.{j}') - d1) / scale), (res + D(f'0.{j}') - d1)
#                     for k in range(10 * (j - 1), 100):
#                         if (f + D(f'0.0{k}')) == (s - D(f'0.0{k}') / scale) == (res + D(f'0.0{k}')):
#                             res += D(f'0.0{k}')
#                             return res
#                         elif (s - D(f'0.0{k}') / scale) < (res + D(f'0.0{k}')):
#                             f, s, res = (f + D(f'0.0{k}') - d2), (s - (D(f'0.0{k}') - d2) / scale), (
#                                     res + D(f'0.0{k}') - d2)
#                             for h in range(1, k * 10):
#                                 if (f + D(f'0.00{h}')) == (s - D(f'0.00{h}') / scale) == (res + D(f'0.00{h}')):
#                                     res += D(f'0.00{h}')
#                                     return res
#                                 elif (s - D(f'0.00{h}') / scale) < (res + D(f'0.00{h}')):
#                                     f, s, res = (f + D(f'0.00{h}') - d3), (s - (D(f'0.00{h}') - d3) / scale), (
#                                             res + D(f'0.00{h}') - d3)
#                                     for o in range(1, h * 10):
#                                         if ((f + D(f'0.000{o}')) == (s - D(f'0.000{o}') / scale) == (
#                                                 res + D(f'0.000{o}'))) or (s - D(f'0.000{o}') / scale) < (
#                                                 res + D(f'0.000{o}')):
#                                             res += D(f'0.000{o}')
#                                             return res
#
#
# if (x0[0] + x1[0]) / 2 == x / 2 and (y0[1] + y1[1]) / 2 == y / 2:
#     print(eval(f'{(x / 2, 4):.4f}'), eval(f'{(y / 2, 4):.4f})'))
# else:
#     print(eval(f'{float(paper(rect[0])):.4f}'), eval(f'{float(paper(rect[1])):.4f}'))

# paper = (5.0000, 2.5000)
#
# end, that_is =  x0, (0,0)
# if (x0[0]+ x1[0]) / 2 == x /2 and (y0[1]+ y1[1]) /2 == y / 2:
#     print(*paper)
# elif x0[0]> x1[0] and x0[1] > x1[1]:
#     for i in range(1,10):
#         end[0] -= i * 0.1
#         that_is[0] += i * 0.1 * scale
#         if end[0] == that_is[0]:
#             break
#         elif  end[0] < that_is[0]:
#             end[0] += i * 0.1
#             that_is[0] -= 0, i * scale
#             for j in range(1,100):
#                 end[0] -= 0, 0j
#                 that_is[0] += 0, 0j * scale
#                 if end[0] == that_is[0]:
#                     break
#                 elif end[0] < that_is[0]:
#                     end[0] += 0, 0j
#                     that_is[0] -= 0, 0j * scale
#                     for k in range(1,1000):
#                         end[0] -= 0, 00k
#                         that_is[0] += 0, 00k * scale
#                         if end[0] == that_is[0]:
#                             break
# print(that_is)
'''экономия на обедах'''

# first try ===================

# total, start = 0, 0
# lanches = []
# coupons = dict()
# result = 0
#
# for i in range(n := int(input())):
#     lanches.append( tmp := int(input()))
#     total += tmp
# k = total // 100
#
# for i in range(k):
#     coupons[i] = []
#     for j in lanches[start:]:
#         coupons[i].append(j)
#         start = lanches.index(j)+1
#         if sum(coupons[i]) > 99:
#             break
# coupons[len] = [0]
# total = 0
# for i in range(1,len(coupons)):
#
#     try:
#         to_del = max(list(coupons[i]))
#         del coupons[i][(coupons[i]).index(to_del)]
#         while sum(coupons[i]) < 100:
#             coupons[i].append((coupons[i+1][0]))
#             del coupons[i+1][0]
#
#     except Exception as e:
#         pass
# for i in coupons.values():
#     total += sum(i)
# print(total)

# second try ===================

# total, start = 0, 0
# lanches = []
# for i in range(n := int(input())):
#     lanches.append( tmp := int(input()))
# max_coupons, del_max_price = 0, 0
#
# for _ in range(len(lanches)):
#     if lanches:
#         del_max_price += lanches[0]
#         max_coupons += lanches[0]
#         lanches.remove(lanches[0])
#         if max_coupons> 100:
#             max_coupons -= 100
#             if lanches:
#                 del lanches[lanches.index(max(lanches))]
#
# print(del_max_price)
'''сколько сумм монет в кошельке'''
# from itertools import combinations_with_replacement
#
# N = int(input())
# coins =  list(map(int, input().split()))
# list_sum = []
# for i in range(1, len(coins)+1):
#     for j in range(N):
#         for k in combinations_with_replacement(coins, i):
#             if k not in list_sum and sum(k) <= N-1:
#                 list_sum.append(k)
# print(list_sum)

'''разрезать торт на 2 ровные части вертикально'''

N = int(input())
x, y = [], []
for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    x.append(tmp[0])
    y.append(tmp[1])


def sum_sides(x1, y1, x2, y2):
    print(((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5)
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5


if min(x) != x[0]:
    for _ in range(x.index(min(x))):
        x.append(x.pop(0))
        y.append(y.pop(0))

perimetr = 0
for i in range(N - 1):
    perimetr += sum_sides(x[i], y[i], x[i + 1], y[i + 1])
perimetr += sum_sides(x[-1], y[-1], x[0], y[0])

list_x, list_y = [], []
angle = 0

left_side_x = [0, 1]


def k_angle(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return [(x, k * x + b) for x in range(x1, x2 + 1)]


try:
    list_left = k_angle(x[left_side_x[-1]], y[left_side_x[-1]], x[left_side_x[-1] + 1], y[left_side_x[-1] + 1])
    list_right = k_angle(x[left_side_x[0]], y[left_side_x[0]], x[left_side_x[0] - 1], y[left_side_x[0] - 1])
except ZeroDivisionError:
    left_side_x = [-1, 0]
    list_left = k_angle(x[left_side_x[-1]], y[left_side_x[-1]], x[left_side_x[-1] + 1], y[left_side_x[-1] + 1])
    list_right = k_angle(x[left_side_x[0]], y[left_side_x[0]], x[left_side_x[0] - 1], y[left_side_x[0] - 1])
n_rise = 0
half_perimetr = 0

while half_perimetr < perimetr / 2:
    half_perimetr = 0
    del list_left[0]
    del list_right[0]
    if -1 in left_side_x:
        x[1], x[-1] = x[-1], x[1]
        y[1], y[-1] = y[-1], y[1]
        half_perimetr += sum_sides(x[0], y[0], x[-1], y[-1])

        if len(left_side_x) > 1:

            half_perimetr += sum_sides(x[1], y[1], list_left[0][0], list_left[0][1])
            half_perimetr += sum_sides(x[0], y[0], list_right[0][0], list_right[0][1])

        else:
            half_perimetr += sum_sides(x[1], y[1], list_left[0][0], list_left[0][1])
            half_perimetr += sum_sides(x[0], y[0], list_right[0][0], list_right[0][1])

    else:
        half_perimetr += sum_sides(x[0], y[0], x[1], y[1])

        half_perimetr += sum_sides(x[1], y[1], list_left[0][0], list_left[0][1])

print(list_right[0][1])
