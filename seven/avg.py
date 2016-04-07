# coding=utf-8
__author__ = 'zjutK'


def avg(first, *rest,**kwargs):

    print(rest)
    print(kwargs)
    print(first + sum(rest))


avg(1, 2)
avg(1, 2, 3, 4,color="blue",test="haha")
