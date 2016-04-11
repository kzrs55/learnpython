# coding=utf-8
__author__ = 'zjutK'
'''运算符重载实例'''


class Number(object):
    def __init__(self, data):
        self.data = data

    def __sub__(self, other):
        return Number(self.data - other)  # 递归


if __name__ == '__main__':
    x = Number(5)
    y = x - 2
    print(y)
    print(y.data)
