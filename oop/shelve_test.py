# coding=utf-8
from oop.person import Person
import shelve

__author__ = 'zjutK'

'''利用shelve进行类对象存储'''

bob = Person('bob smith', job='teacher', pay=100)
tom = Person('tom smith', job='student', pay=150)
kent = Person('kent jones', job='teacher', pay=100)

db = shelve.open('person_db')
for _object in (bob, tom, kent):
    db[_object.name] = _object
db.close()

