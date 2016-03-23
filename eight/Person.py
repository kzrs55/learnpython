#coding=utf-8
__author__ = 'zjutK'
class Person:
    def __init__(self,first_name):
        self.first_name=first_name

    @property
    def first_name(self):
        return self._first_name;

    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise "type must be str"
        self._first_name=value

    @first_name.deleter
    def first_name(self):
        raise "can't delete"

a=Person("zhou")
a.first_name=11
print(a.first_name)