# coding:utf8
import sys


def sieve(n):
    # computer primes using sieve eratosthenes
    x = [1] * n
    x[1] = 0

    for i in range(2, n/2):
        j = 2 * i
        while j < n:
            x[j] = 0  # 把所有i的倍数筛除
            j += i  # 下一个i的倍数

    return x


def prime(n, x):
    # Find nth prime
    i = 1  # 初始化为1
    j = 1

    while j <= n:
        if x[i] == 1:  # 在布尔数组中寻找第n个标记为1的数
            j += 1
        i += 1

    return i-1  # 前面循环中i多加了一次，返回时需要减1

l = sieve(120)

for k in range(1, l.count(1)):
    print prime(k, l)
