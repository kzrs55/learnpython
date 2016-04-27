# coding=utf-8
import time
from threading import Thread

__author__ = 'zjutK'


class CountdownTask(object):
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


if __name__ == '__main__':
    c = CountdownTask()
    t = Thread(target=c.run, args=(10,))
    t.start()
