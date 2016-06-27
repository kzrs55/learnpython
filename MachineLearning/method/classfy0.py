# -*- coding: utf-8 -*-
import operator
from numpy import tile, array


def classfy0(inX, dataSet, labels, k):
    dateSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dateSetSize - 1)) - dataSet
    sqdiffMat = diffMat ** 2
    sqDistances = sqdiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 选择距离最小的k个点
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 排序
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


if __name__ == '__main__':
    group,labels = createDataSet()
    classfy0([0,0],group,labels,3)