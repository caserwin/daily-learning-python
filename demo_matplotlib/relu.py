# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 下午2:45
# @Author  : yidxue
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


def relu(x):
    # 直接返回sigmoid函数
    return [max(0, i) for i in x]


def relu_derivative(x):
    # 直接返回sigmoid函数
    return [1 if (i >= 0) else 0 for i in x]


def plot_relu():
    # param:起点，终点，间距
    x = np.arange(-2, 2, 0.001)
    sig = relu(x)
    print(sig)
    sig_der = relu_derivative(x)
    print(sig_der)

    plt.plot(x, sig)
    plt.plot(x, sig_der)
    plt.legend((u'relu', u'relu derivative'), loc='best')

    plt.savefig("activation_function2.png")
    plt.show()


if __name__ == '__main__':
    plot_relu()
