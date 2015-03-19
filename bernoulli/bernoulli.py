#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import numpy as np
from sklearn.naive_bayes import BernoulliNB

def test():
    X = np.random.randint(2, size=(6, 100))
    Y = np.array([1, 2, 3, 4, 4, 5])

    clf = BernoulliNB()
    clf.fit(X, Y)
    print clf.predict(X[2])

def main():
    print 'enter main...'
    test()

if __name__ == "__main__":
    main()