#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
from sklearn import datasets
import matplotlib.pyplot as plt


def test():
    plt.subplot(231)
    scatter_plot(0, 1)
    plt.subplot(232)
    scatter_plot(0, 2)
    plt.subplot(233)
    scatter_plot(0, 3)
    plt.subplot(234)
    scatter_plot(1, 2)
    plt.subplot(235)
    scatter_plot(1, 3)
    plt.subplot(236)
    scatter_plot(2, 3)
    plt.show()


def scatter_plot(dim1, dim2):
    iris = datasets.load_iris()
    irisFeatures = iris["data"]
    irisLabels = iris["target"]
    for t, marker, color in zip(xrange(3), ">ox", "rgb"):
        # zip()接受任意多个序列参数，返回一个元组tuple列表
        # 用不同的标记和颜色画出每种品种iris花朵的前两维数据
        # We plot each class on its own to get different colored markers
        plt.scatter(irisFeatures[irisLabels == t, dim1],
                    irisFeatures[irisLabels == t, dim2], marker=marker, c=color)
    dim_meaning = {0: 'setal length', 1: 'setal width', 2: 'petal length', 3: 'petal width'}
    plt.xlabel(dim_meaning.get(dim1))
    plt.ylabel(dim_meaning.get(dim2))

def main():
    print 'enter main...'
    test()

if __name__ == "__main__":
    main()