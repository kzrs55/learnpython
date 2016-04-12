# coding=utf-8
from tkinter import Button

__author__ = 'zjutK'
'''__call__使用'''


class Call(object):
    def __call__(self, *args, **kwargs):
        print('Called:', args, kwargs)


class ColorBack(object):
    def __init__(self, color):
        self.color = color

    def __call__(self, *args, **kwargs):
        print('turn', self.color)


if __name__ == '__main__':
    C = Call()
    C(1, 2, 3)  # Called: (1, 2, 3) {}
    C(1, 2, 3, a='qq', b='lll')  # Called: (1, 2, 3) {'b': 'lll', 'a': 'qq'}
    cb1 = ColorBack('blue')
    cb2 = ColorBack('red')
    print(cb1())
    B1 = Button(command=cb1)
    print(B1)
