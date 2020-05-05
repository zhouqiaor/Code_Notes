# coding=utf-8
import time

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

t = time.time()
fib(40)
print(time.time() - t)