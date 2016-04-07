# coding=utf-8
__author__ = 'zjutK'
'''
外观模式
'''


class Function1(object):
    name = "do_something"

    def __init__(self):
        pass

    def do_something(self):
        print(self.name)


class Function2(object):
    name = "do_anything"

    def __init__(self):
        pass

    def do_anything(self):
        print(self.name)


class Facade(object):
    def __init__(self):
        self.module_one = Function1()
        self.module_two = Function2()

    def creat_module_one(self):
        self.module_one.do_something()
        self.module_two.do_anything()

    def creat_module_two(self):
        self.module_two.do_anything()


