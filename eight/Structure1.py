#coding=utf-8
import math

__author__ = 'zjutK'

class structure:
    _fields=[]

    def __init__(self,*args):
        if len(args)!=len(self._fields):
            raise TypeError

        for name,value in zip(self._fields,args):
            setattr(self,name,value)


class Stock(structure):
    _fields = ['name','share','price']


class Point(structure):
    _fields = ['x','y']


class Circle(structure):
    _fields = ['radius']

    def area(self):
        return math.pi*self.radius**2

s=Stock('ACME',22,99)
print(s)