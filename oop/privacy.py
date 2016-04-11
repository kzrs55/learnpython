# coding=utf-8
__author__ = 'zjutK'
'''模拟实例属性的私有性'''


class PrivateExc(Exception):
    pass


class Privacy(object):
    def __setattr__(self, instance, value):
        if instance in self.privates:
            raise PrivateExc(instance, self)
        else:
            self.__dict__[instance] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__init__['name'] = 'tom'


if __name__ == '__main__':
    x = Test1()
    y = Test2()
    x.name = 'Bob'
    y.name = 'Sue'
