# coding=utf-8
__author__ = 'zjutK'
'''通过嵌入拓展类型'''


class Set(object):
    def __init__(self, value=[]):
        self.data = []
        self.contact(value)

    # 将value的值复制到data中,并且使得这些值不重复
    def contact(self, value):
        for x in value:
            if x not in self.data:
                self.data.append(x)

    # 比较other与data中的值,将两者共同的值添加进other
    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    # 比较other与data的值,将两者不同的值添加进other
    def union(self, other):
        res = self.data[:]
        for x in other:
            if x not in res:
                res.append(x)
        return Set(res)

    # len(self)
    def __len__(self):
        return len(self.data)

    # self[i]
    def __getitem__(self, item):
        return self.data[item]

    # self & other
    def __and__(self, other):
        return self.intersect(other)

    # self ! other
    def __or__(self, other):
        return self.union(other)

    # self print()
    def __repr__(self):
        return 'Set:' + repr(self.data)


if __name__ == '__main__':
    x = Set([1, 3, 5, 7])
    print(x.union(Set([1, 4, 7])))  # Set:[1, 3, 5, 7, 4]
    print(x | Set([1, 4, 6]))  # Set:[1, 3, 5, 7, 4, 6]
