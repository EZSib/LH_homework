import threading
import time
import asyncio
import math

def fctrl(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res
start1 = time.time()
fctrl(200000)
end1 = time.time() - start1
print(end1)

start2 = time.time()
math.factorial(200000)
end2 = time.time() - start2
print(end2)