# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 下午1:54
# @Author  : yidxue
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


def sigmoid(x):
    # 直接返回sigmoid函数
    return 1. / (1. + np.exp(-x))


def sigmoid_derivative(x):
    # 直接返回sigmoid函数
    return (1. / (1. + np.exp(-x))) * (1 - 1. / (1. + np.exp(-x)))


def plot_sigmoid():
    # param:起点，终点，间距
    x = np.arange(-10, 10, 0.2)
    sig = sigmoid(x)
    sig_der = sigmoid_derivative(x)

    plt.scatter(x, sig, label='sigmoid', c='red')
    plt.scatter(x, sig_der, label='sigmoid derivative', c='green')
    plt.legend((u'sigmoid', u'sigmoid derivative'), loc='best')

    plt.savefig("activation_function1.png")
    plt.show()


if __name__ == '__main__':
    plot_sigmoid()
