#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""

from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
import pickle

def test():
    iris = datasets.load_iris()
    print iris.data.shape
    print iris.data[:10]
    print iris.target

def gaussiannb():
    iris = datasets.load_iris()
    clf = GaussianNB()
    clf.fit(iris.data[1:149, :], iris.target[1:149])
    print iris.data[1:149, :].shape
    print clf.predict(iris.data[0, :])
    print clf.predict_proba(iris.data[0, :])
    print clf.predict_proba(iris.data[149, :])

    # save model
    pickle.dump(clf, open('bayes.pk', 'wb'))
    # test pickle result
    clf2 = pickle.load(open('bayes.pk', 'rb'))
    print clf2.predict(iris.data[0, :])
    print clf2.predict_proba(iris.data[0, :])

    print clf2.predict(iris.data[149, :])
    print clf2.predict_proba(iris.data[149, :])

def main():
    print 'enter main...'
    test()
    #gaussiannb()

if __name__ == "__main__":
    main()