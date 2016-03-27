#coding=utf-8
__author__ = 'zjutK'
'''
对于一个字符串，和字符串中的某一位置，请设计一个算法，将包括i位置在内的左侧部分移动到右边，将右侧部分移动到左边。
给定字符串A和它的长度n以及特定位置p，请返回旋转后的结果。
测试样例：
"ABCDEFGH",8,4
返回："FGHABCDE"
'''

def rotateString(A, n, p):
    return A[p+1:n]+A[:p+1]


if __name__ == '__main__':
    print(rotateString('ABCDEFGH',8,4))
