# coding=utf-8
__author__ = 'zjutK'
'''python3中如何使用注解函数'''


def func(a: float = 10, b: 'spam' = 4, c: (1, 10) = 5) -> int:
    return a + b + c

if __name__ == '__main__':
    print(func(1,3,11))
    print(func.__annotations__) # 查看func注释