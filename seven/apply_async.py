#coding=utf-8
__author__ = 'zjutK'
def apply_async(func,args,*,callback):
    result=func(*args)
    callback(result)


def add(a,b):
    return a+b

def print_result(result):
    print('Got: %s' %result)


apply_async(add,(2,3),callback=print_result)