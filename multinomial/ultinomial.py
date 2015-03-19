#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import numpy as np
from sklearn.naive_bayes import MultinomialNB


def test():
    X = np.random.randint(5, size=(6, 100))
    y = np.array([1, 2, 3, 4, 5, 6])
    clf = MultinomialNB()
    clf.fit(X, y)
    print clf.predict(X[2])

def main():
    print 'enter main...'
    test()


if __name__ == "__main__":
    main()