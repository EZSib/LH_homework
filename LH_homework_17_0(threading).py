import threading

import time

# def hello(name):
#     time.sleep(2)
#     print(f'i am {name}')
#
# t = threading.Thread(target=hello, args='t1', name= 't1')
#
# t.start()
# t.join()

def sqrs(start, stop):
    res = 0
    for x in range(start, stop):
        res += x**2
    return res

def many_thrds(n):
    threads = []
    for i in range(1, n+1):
        t = threading.Thread(target=sqrs, args= (100000 * (i-1) // n, 100000 * (i) // n))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# t1_start = time.time()
# many_thrds(16)
# t1_end = time.time() - t1_start
#
# t2_start = time.time()
# sqrs(0, 100000)
# t2_end = time.time() - t2_start
#
# print('time 1',t1_end)
# print('time 2',t2_end)

def workers(t, name):
    time.sleep(t)
    print(f'i slept {t} sec my name{name}')


def many_thrds1(n):
    threads = []
    for i in range(1, n+1):
        t = threading.Thread(target=workers, args=(3, str(i)))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

t1_start = time.time()
many_thrds1(10)
t1_end = time.time() - t1_start

print('time 1',t1_end)

# t2_start = time.time()
# for i in range(10):
#     workers(3, i)
# t2_end = time.time() - t2_start
#
# print('time 2',t2_end)

lock = threading.Lock() #блокировка

def workers_w_l(t, name):
    time.sleep(t)
    with lock:
        print(f'i slept {t} sec my name{name}')

def many_thrds2(n):
    threads = []
    for i in range(1, n+1):
        t = threading.Thread(target=workers_w_l, args=(3, str(i)))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

t3_start = time.time()
many_thrds2(10)
t3_end = time.time() - t3_start

print('time 3',t3_end)