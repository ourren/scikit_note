#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import numpy
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB


def testdata():
    iris = datasets.load_iris()
    print iris.feature_names
    # print iris.data
    print iris.data.size
    print iris.target_names
    print iris.target


def pre_height():
    iris = datasets.load_iris()
    clf = GaussianNB()
    clf.fit(iris.data, iris.target)
    print clf.predict(iris.data[0])
    data = numpy.array([6, 4, 6, 2])
    print clf.predict(data)

def main():
    print 'enter main...'
    pre_height()


if __name__ == "__main__":
    main()