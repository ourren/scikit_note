#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import scipy as sp
import matplotlib.pyplot as plt


def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)


def main():
    print 'enter main...'
    data = sp.genfromtxt("web_traffic.tsv", delimiter='\t')
    x = data[:, 0]
    y = data[:, 1]
    print sp.sum(sp.isnan(y))
    x = x[~sp.isnan(y)]
    y = y[~sp.isnan(y)]

    # plt.scatter(x, y)
    # plt.title('Web traffic over the last month')
    # plt.xlabel("time")
    # plt.ylabel("Hits/hour")
    # plt.xticks([W * 7 * 24 for W in range(10)], )  # set label for x
    # plt.autoscale(tight=True)
    # plt.grid()
    # plt.show()

    fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
    print(fp1)
    f1 = sp.poly1d(fp1)
    fx = sp.linspace(0, x[-1], 1000)
    plt.scatter(x, y)
    plt.title("Web traffic over the last month")
    plt.xlabel("Time")
    plt.ylabel("Hits/hour")
    plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
    plt.autoscale(tight=True)
    plt.grid()
    plt.plot(fx, f1(fx), linewidth=4)
    plt.legend(["d=%i" % f1.order], loc="upper left")
    plt.show()


if __name__ == "__main__":
    main()