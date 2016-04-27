# coding=utf-8
from threading import Thread, Event

import time

__author__ = 'zjutK'


# 继承Thread类引入额外的继承关系

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def countdown(self, started_evt):
        print('countdown starting')
        started_evt.set()
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)


def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


if __name__ == '__main__':
    c = CountdownThread(5)
    # c.start()

    # import multiprocessing
    #
    # p = multiprocessing.Process(target=c.run)   #让代码单独在进程中运行
    # p.start()
    started_evt = Event()
    print('lauching')
    t = Thread(target=c.countdown, args=(started_evt,))  # 线程同步问题
    t.start()
    started_evt.wait()
    print('counting is running')
