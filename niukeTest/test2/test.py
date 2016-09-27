# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    boolean = True
    for i in range(12):
        k = (n - 6 * i) % 8
        if k == 0:
            print i + (n - 6 * i) / 8
            boolean = False
            break
        if k<0:
            break
    if boolean:
        print -1

