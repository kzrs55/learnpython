#coding=utf-8
from time import sleep, time

__author__ = 'zjutK'
'''
yield 有什么优点,面试问道yield与list的区别,有点懵,所有的东西都存在内存中的。
但是当你的iterable很大，例如这个list有一千万个元素的时候，就不是一个很令人开心的事情了。
'''

class A(object):
    def __init__(self,i):
        self.i =i



if __name__ == '__main__':
    ss =[A(i) for i in range(5)]   #返回的是迭代器
    st =(A(i) for i in range(5))   #返回的是生成器
    tuple = (1,2,3,4,5,6)

    for i in ss:
        print i

    for i in range(5):
        print st.next()
