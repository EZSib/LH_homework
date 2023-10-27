from sys import *
'''a+b'''
# a,b = input().split()
# print(int(a)+int(b))

'''a+b txt'''
# with open('input.txt',encoding='utf8' ) as t:
#     a,b = map(int, t.readline().split())
#     with open('output.txt', 'w+', encoding='utf8') as out:
#         out.write(f'{a+b}')

'''a+b stdin, stdout'''

# for i in stdin:
#     a,b = map(int, i.split())
#     stdout.write(f'{a + b}')

# from sys import *
# j = stdin.readline().strip()
# s = stdin.readline().strip()
# cnt = 0
# for i in s:
#     if i in j:
#         cnt += 1
# print(cnt)

'''1.Сколько жили ящеры '''
'''слущает отсутствие високосных, чтобы пользоваться calendar or datetime '''
# mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# sec_in_day = 60*60*24
# start = list(map(int, input().split()))
# end = list(map(int, input().split()))
# start[0],end[0] = start[0] * 365 * 24 * 60 * 60, end[0] * 365 * 24 * 60 * 60
# start[1],end[1] = (sum(mon[:start[1]-1]) + start[2]) * 24 * 60 * 60, (sum(mon[:end[1]-1]) + end[2]) * 24 * 60 * 60
# start[2], end[2] = 0, 0
# start[3], end[3] = start[3] * 60 * 60, end[3] * 60 * 60
# start[4], end[4] = start[4] * 60, end[4] * 60
#
# print(f'{(sum(end) - sum(start)) // sec_in_day} {(sum(end) - sum(start)) % sec_in_day}')

'''2. Две колоды карт, вычисляем разнообразие'''
# from collections import Counter as C
#
# iterations = int(input().split()[2])
#
# A = C(input().split())
# B = C(input().split())
# print(A)
# print(B)
# res = []
# for _ in range(iterations):
#     tmp = input().split()
#     if tmp[0] == '1':
#         eval(tmp[1]).update(list([tmp[2]]))
#     else:
#         eval(tmp[1]).subtract(list([tmp[2]]))
#
#     print('a', A)
#     print('b', B)
#     print(max((A,B), key=len) - min((A,B), key=len), min((A,B), key=len) - max((A,B), key=len))
#     res.append(len(max((A,B), key=len) - min((A,B), key=len))+ len(min((A,B), key=len) - max((A,B), key=len)))
#
# print(*[int(i) for i in res])

# '''Симулятор скл'''
#
# row, col, limit = map(int, input().split())
# col_name = {i:[] for i in input().split()}
#
# matrix = []
# cnt_row = 0
# res = {i:[] for i in range(row)}
# for i in range(row):
#     matrix.append(list(map(int, input().split())))
# for rows in col_name:
#     for ind,num in enumerate(matrix):
#         col_name[rows].append((ind, num[cnt_row]))
#     cnt_row += 1
# for cond in range(limit):
#     dct_char, h_or_l, n = input().split()
#     col_name[dct_char] = list(filter(lambda x: eval(f'{x[1]} {h_or_l} {n}') ,col_name[dct_char]))
# for i in range(row):
#     for j in col_name.values():
#         for k in j:
#             if k[0] == i:
#                 res[i].append(k[1])
# print(sum(list(map(sum,(filter(lambda x: len(x) == row, res.values()))))))
#
# print(res)

'''Равны по индексам'''

n = int(input())
list_ar  = []
cnt = 0
for i in range(n*2):
    list_ar.append(list(map(int, input().split())))
list_ar = list_ar[1::2]
list_ar.sort(key=len)
print(list_ar)

for i in range(n):
    for j in range(n):
        if
