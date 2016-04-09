# coding=utf-8
__author__ = 'zjutK'
'''利用递归处理任意结构
[1,2,3,[1,2,3],[1,2,[1,3],]]元素求和
'''


def sum_tree(list_1):
    sum_1 = 0
    for i in list_1:
        if not isinstance(i, list):
            sum_1 += i
        else:
            sum_1 += sum_tree(i)
    return sum_1


if __name__ == '__main__':
    list_1 = [1, 2, 3, [1, 2, 3], [1, 2, [1, 3], ]]
    print(sum_tree(list_1))
