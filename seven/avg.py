#coding=utf-8
__author__ = 'zjutK'

def avg(first,*rest):
    print(first+sum(rest))


avg(1,2)
avg(1,2,3,4)