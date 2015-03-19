#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import nltk
from random import shuffle
from sklearn.svm import LinearSVC
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline

def dialogue_act_features(sentence):
    """
        Extracts a set of features from a message.
    """
    features = {}
    tokens = nltk.word_tokenize(sentence)
    for t in tokens:
        features['contains(%s)' % t.lower()] = True
    return features


def main():
    print 'enter main...'
    # data structure representing the XML annotation for each post
    posts = nltk.corpus.nps_chat.xml_posts()
    # label set
    cls_set = ['Emotion', 'ynQuestion', 'yAnswer', 'Continuer',
               'whQuestion', 'System', 'Accept', 'Clarify', 'Emphasis',
               'nAnswer', 'Greet', 'Statement', 'Reject', 'Bye', 'Other']
    featuresets = []  # list of tuples of the form (post, features)
    for post in posts:  # applying the feature extractor to each post
        # post.get('class') is the label of the current post
        featuresets.append((dialogue_act_features(post.text), cls_set.index(post.get('class'))))

    shuffle(featuresets)
    size = int(len(featuresets) * .1)  # 10% is used for the test set
    train = featuresets[size:]
    test = featuresets[:size]
    # SVM with a Linear Kernel and default parameters
    clf = SklearnClassifier(LinearSVC())
    clf.train(train)
    test_skl = []
    t_test_skl = []
    for d in test:
        test_skl.append(d[0])
        t_test_skl.append(d[1])
    # run the classifier on the train test
    print t_test_skl

    p = clf.classify_many(test_skl)
    # getting a full report
    print classification_report(t_test_skl, p, labels=list(set(t_test_skl)), target_names=cls_set)

if __name__ == "__main__":
    main()