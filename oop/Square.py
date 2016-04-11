# coding=utf-8
__author__ = 'zjutK'
'''利用迭代器iter生成平方值'''


class Square(object):
    def __init__(self, value, stop):
        self.value = value - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        else:
            self.value += 1
            return self.value ** 2


if __name__ == '__main__':
    test = Square(1, 9)
    for i in test:
        print(i)
