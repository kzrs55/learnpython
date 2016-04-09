# coding=utf-8
__author__ = 'zjutK'
'''前向引用实例'''

# func_1()   # name 'func_1' is not defined


def func_1():
    print(func_2())


# func_1()   # name 'func_2' is not defined


def func_2():
    return 'hello'

func_1()  # ok
