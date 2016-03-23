#coding=utf-8
__author__ = 'zjutK'

class Base:
    def __init__(self):
        print("base.init")

class A(Base):
    def __init__(self):
        super().__init__()
        print("A.init")

class B( Base ):
    def __init__(self):
        super().__init__()
        print("B.init")


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("c.init")


print(C())