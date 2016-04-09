# coding=utf-8
__author__ = 'zjutK'
'''send next在生成器中的使用'''


def gen(number):
    for i in range(number):
        yield i ** 2


if __name__ == '__main__':
    G = gen(10)
    print(next(G))
    G.send(77)
    G.send(88)  # send方法生成一系列结果的下一个元素
    next(G)