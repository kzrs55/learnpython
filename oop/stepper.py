# coding=utf-8
__author__ = 'zjutK'
'''getitem索引运算'''


class Stepper(object):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        return self.data[item]


if __name__ == '__main__':
    X = Stepper('spam')
    print(X[1])
    for i in X:
        print(i,end=' ')
