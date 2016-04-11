# coding=utf-8
__author__ = 'zjutK'
'''利用递归求类树'''


def class_tree(cls, indent):
    print('.' * indent + cls.__name__)
    for super_cls in cls.__bases__:
        class_tree(super_cls, indent + 3)


def instance_tree(inst):
    print('tree of %s' % inst)
    class_tree(inst.__class__, 3)


if __name__ == '__main__':
    class A:
        pass

    class B(A):
        pass


    class C(A):
        pass


    class D(B, C):
        pass


    class E:
        pass


    class F(D, E):
        pass


    instance_tree(B())
    instance_tree(F())
