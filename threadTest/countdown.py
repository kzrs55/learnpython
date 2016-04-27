# coding=utf-8
__author__ = 'zjutK'

import time


def CountDown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# 线程使用

from  threading import Thread

t = Thread(target=CountDown, args=(10,))
t.start()
if t.is_alive():
    print("still running")
else:
    print("complete")
