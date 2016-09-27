# -*- coding: utf-8 -*-

def fib(max):
    n,a,b=0,1,1
    while n<max:
        print a
        a,b = b,a+b
        n+=1
if __name__ == '__main__':
    fib(6)