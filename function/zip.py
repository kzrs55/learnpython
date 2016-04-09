# coding=utf-8
__author__ = 'zjutK'
'''zip函数的高级使用'''


def my_app(func, *seq):
    res = []
    for args in zip(*seq):
        res.append(func(*args))
    print(res)
    return res


# 上述函数等价于
def my_map(func, *seq):
    return [func(*args) for args in zip(*seq)]


if __name__ == '__main__':
    my_app(abs, [-11, -2, 3, 4, 5])
    my_app(pow, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
