#coding=utf-8
__author__ = 'zjutK'

'''
题目描述

对于一个矩阵，请设计一个算法，将元素按“之”字形打印。具体见样例。
给定一个整数矩阵mat，以及他的维数nxm，请返回一个数组，其中元素依次为打印的数字。
测试样例：
[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],4,3
返回：[1,2,3,6,5,4,7,8,9,12,11,10]
'''
def printMatrix(mat, n, m):
    for i in range(1,n):
        if i%2==1:
            mat[i].reverse()
        mat[0].extend(mat[i])
    return mat[0]

if __name__ == '__main__':
    print(printMatrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],4,3))