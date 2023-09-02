# '''задача с магазином револьверов '''
# n , money = map(int, input().split())
# list_rev = list(map(int, input().split()))
# list_rev_res = list(map(lambda x: x-money+10000000000 if x-money <= 0 else 0, list_rev))
# if any(list_rev_res):
#     print(list_rev[list_rev_res.index(max(list_rev_res))])
# else:
#     print(0)
'''задача с количеством слова в строке'''
# 'sheriff'
# s = input()
# cnt = 0
# res = s
# while len(res) - len(s) == 0 or (len(res) - len(s)) % 7 == 0:
#     s = s.replace('s','',1)
#     s = s.replace('h','',1)
#     s = s.replace('e','',1)
#     s = s.replace('r','',1)
#     s = s.replace('i','',1)
#     s = s.replace('f','',2)
#     if (len(res) - len(s)) % 7:
#         break
#     cnt +=1
# print(cnt)

'''задача где надо отсортировать отрезок чисел, чтобы убедиться в равенстве с результирующим списком'''
# n = int(input())
# bob = input().replace(' ', '')
# win = input().replace(' ', '')
# if bob == win:
#     print('YES')
#     quit()
# start, end = -1, 0
# for i in range(n):
#     if bob[i] == win[i]:
#         start += 1
#     else:
#         break
# for i in range(1, n + 1):
#     if bob[-i] == win[-i]:
#         end -= 1
#     else:
#         break
# if end == 0:
#     bob = bob[:start + 1] + ''.join(sorted(bob[start + 1:]))
# else:
#     bob = bob[:start + 1] + ''.join(sorted(bob[start + 1: end])) + bob[end:]
# print('YES' if bob == win else 'NO')

'''как честный ковбой в банк ходил за наличкой (набрать сумму заданными номиналами(макс кол-во купюр 2))'''
# from itertools import *
#
# cash, nom_pcs = map(int, input().split())
# all_cash = list(map(int, input().split())) * 2
# set_nom = list(set(all_cash))
# if sum(all_cash) < cash:
#     quit(print(-1))
# if sum(set_nom) == cash:
#     print(len(set_nom))
#     quit(print(*sorted(set_nom)))
# if sum(all_cash) == cash:
#     print(len(all_cash))
#     quit(print(all_cash))
#
#
# def res(sq):
#     for i in range(1, len(sq) + 1):
#         a = combinations(sq, i)
#         for j in a:
#             if sum(j) == cash:
#                 print(len(j))
#                 quit(print(*j))
#     print(-1)
#
#
# res(all_cash)

'''дух разрушающий дороги но не трогающий территориальное устройство'''

# cities, roads_n = map(int, input().split())
# states_n = cities - 1
# roads = []
#
# for i in range(roads_n):
#     roads.append(list(map(int, input().split())))
# states = dict()
# roads = list(map(lambda x: [set(x[:2]), x[2]], roads))
# tmp_states = roads
# for i in range(1, states_n + 1):
#     try:
#         states[i] = tmp_states[0]
#         del tmp_states[0]
#         for j in tmp_states:
#             if states[i][0] == j[0]:
#                 states[i].append(j[1])
#                 del tmp_states[tmp_states.index(j)]
#     except IndexError:
#         pass
# print(min(list(map(lambda x: max(x[1:]) if len(x) > 2 else 100000000000, states.values()))) - 1)

'''банды духов и их вопросы'''
ghost, quest = map(int, input().split())

bands = [str(i) for i in range(1,ghost+1)]

print(bands)

for _ in range(quest):
    a = list(input().split())
    cnt = 0
    if a[0] == '1':
        for i in bands[-1::-1]:
            if cnt:
                break
            if a[1] in i:
                for j in bands[-1::-1]:
                    if cnt:
                        break
                    if a[2] in j:
                        bands.append(i+j)
                        if len(bands[-1]) == 2:
                            bands.remove(a[1])
                            bands.remove(a[2])
                        else:
                            to_remove = (k for k in (i,j) if len(k) == 1)
                            print(*(o for o in (i,j) if len(o) == 1))
                            bands.remove(*to_remove)
                        cnt +=1
        print(bands)
    elif a[0] == '2':
        flag = 'NO'
        for i in bands:
            if a[1]  in i:
                if a[2] in i:
                    flag = 'YES'
                    break
        print(flag)
    elif a[0] == '3':
        for i in bands[-1::-1]:
            if a[1] in i:
                print(len(i))
                break
