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


    # init
    plt.scatter(x, y)
    plt.title("Web traffic over the last month")
    plt.xlabel("Time")
    plt.ylabel("Hits/hour")
    plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
    plt.autoscale(tight=True)
    plt.grid()


    # 1d
    fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
    print(fp1)
    f1 = sp.poly1d(fp1)
    fx = sp.linspace(0, x[-1], 1000)
    plt.plot(fx, f1(fx), linewidth=4, c='m')

    # 3d
    f3 = sp.poly1d(sp.polyfit(x, y, 3))
    plt.plot(x, f3(x), linewidth=4, c='g')

    f5 = sp.poly1d(sp.polyfit(x, y, 5))
    plt.plot(x, f5(x), linewidth=4, c='k')

    f10 = sp.poly1d(sp.polyfit(x, y, 10))
    plt.plot(x, f10(x), linewidth=4, c='r')

    plt.legend(["d=%i" % m for m in [1, 3, 5, 10]], loc="upper left")


    plt.show()


if __name__ == "__main__":
    main()