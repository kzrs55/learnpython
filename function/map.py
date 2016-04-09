# coding=utf-8
from functools import reduce

__author__ = 'zjutK'
'''map,filter,reduce映射的使用'''

count = [1, 2, 3, 4]


def update(_list):
    bar = []
    for i in _list:
        bar.append(i + 10)
    return bar


# map的使用
print(list(map(lambda x: x + 11, count)))
# filter的使用
print(list(filter(lambda x: x % 2 == 0, count)))
# reduce的使用
print(reduce(lambda x, y: x + y, count))  # python3.4reduce已经从全局名字空间中所移除

if __name__ == '__main__':
    print(update(count))
