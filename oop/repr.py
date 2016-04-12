# coding=utf-8
__author__ = 'zjutK'
'''__repr__打印字符串'''


class Adder(object):
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return self.data + other


class AddRepr(Adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data


if __name__ == '__main__':
    x = AddRepr(2)
    print(x + 1)  # run__add__
    print(x)  # run __repr__
