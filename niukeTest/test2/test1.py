# -*- coding: utf-8 -*-
import sys


def f(n):
    while True:
        if n % 2 == 1:
            return n
        n = n / 2


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    sum = 0
    for i in range(n):
        sum += f(i + 1)
    print sum
