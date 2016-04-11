# coding=utf-8
__author__ = 'zjutK'

'''类,封装,多态'''


class Person(object):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    # 返回名字
    def last_name(self):
        return self.name.split(' ')[0]

    # 返回工资
    def give_rise(self, percent):
        self.pay = self.pay * (1 + percent)  # 为转化整形

    def __str__(self):
        return 'Person: %s,%s' % (self.last_name(), self.pay)


class Manager(Person):
    def give_rise(self, percent, bonus=0.1):
        Person.give_rise(self, percent + bonus)  # 通过调用父类的方法,拓展原先的方法,而不是替代他.


if __name__ == '__main__':
    bob = Person('bob smith', job='teacher', pay=100)
    bob.give_rise(0.1)
    print(bob)
    tom = Manager('tom smith', job='student', pay=10)
    print(tom.last_name())
    print(tom)
    for object in (bob,tom):
        object.give_rise(0.1)
        print(object)
