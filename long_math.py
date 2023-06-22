from collections import deque as dq
import time

a = [3,3,3] * 100000
b = [2,2,2] * 10000
coef_gen = ''
def func1(l1, l2):
  def plus1(prv):
    if prv > 0:
      max_len_list[0][prv] = (max_len_list[0][prv] + 1) % 10
      k = max_len_list[0][prv] = (max_len_list[0][prv] + 1) // 10
      max_len_list[0][prv - 1] += k
      if max_len_list[0][prv - 1] >= 9:
        plus1(prv - 1)
    if prv == 0:
      global coef_gen
      max_len_list[0][prv] = (max_len_list[0][prv] + 1) % 10
      coef_gen = '+'

  print(f'количество элементов в а - {len(a)} элементов в б - {len(b)}')
  start_time = time.time()
  prev = max(len(l1), len(l2)) - min(len(l1), len(l2))
  prv = prev - 1
  if len(l1) != len(l2):
    r = min(len(l1), len(l2))
    prev = max(len(l1), len(l2)) - min(len(l1), len(l2))
    print(prev)
    k = 0
    fin = dq()
    max_len_list = dq(filter(lambda x: len(x)== max(len(l1), len(l2)), (l1, l2)))

    for i in range(1, r+1):
      now = (l1[-i]+l2[-i]) %10 +k
      fin.appendleft(now)
      k = (l1[-i]+l2[-i]) //10
    if max_len_list[0][prev-1]+k > 9:
      plus1(prv)
    fin.extend(max_len_list[0][:prev])
    fin.rotate(prev)
    if coef_gen:
      fin.appendleft(1)
    print(f'Время выполнения{time.time() - start_time}')
    return fin
  k = 0
  fin = dq()
  for i in range(1, len(l1)+1):
    now = (l1[-i]+l2[-i]) %10 +k
    fin.appendleft(now)
    k = (l1[-i]+l2[-i]) //10
  if l1[1]+l2[1]>9:
    if l1[0]+l2[0]+1>9:
      fin.appendleft(1)
  print(f'Время выполнения{time.time() - start_time}')
  return fin
# print(int(str(func1(a, b)).replace(',','').replace(' ', '')[7:-2]))

