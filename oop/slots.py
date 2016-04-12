# coding=utf-8
__author__ = 'zjutK'

'''slots实例'''


class Limiter(object):
    __slots__ = ['age', 'name']
    pass


if __name__ == '__main__':
    x = Limiter()
    x.age = 40
    print(x.age)
    x.name = 'haha'
    print(x.name)
    x.job = 'teacher'
    print(x.job)  # AttributeError: 对于不在slots中的属性赋值则会报错
