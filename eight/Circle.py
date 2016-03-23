#coding=utf-8
import math

__author__ = 'zjutK'
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.radius**2*math.pi

    def diameter(self):
        return self.radius*2

    def perimeter(self):
        return self.radius*2*math.pi

c=Circle(4.0)
print(c.area())