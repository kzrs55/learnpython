# coding=utf-8
__author__ = 'zjutK'
'''循环变量的默认参数比较'''


def make_action():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)  # i=i为了让i的值能够传递给嵌套作用域
    return acts


if __name__ == '__main__':
    ss = make_action()
    print(ss[2](2))
