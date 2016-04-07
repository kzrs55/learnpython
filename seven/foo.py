# coding=utf-8
__author__ = 'zjutK'
'''
如何正确使用错误地将表达式作为函数的默认参数
'''


def foo(bar=None):
    if bar is None:
        bar = []
    bar.append("ss")
    print(bar)


if __name__ == '__main__':
    foo()
    foo()
    foo()
