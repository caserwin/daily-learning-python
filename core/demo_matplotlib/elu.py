# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 下午2:57
# @Author  : yidxue
import matplotlib.pyplot as plt
import numpy as np
import math

a = 0.3


def elu(x):
    # 直接返回sigmoid函数
    return [i if (i > 0) else a * (math.exp(i) - 1) for i in x]


def elu_derivative(x):
    # 直接返回sigmoid函数
    return [1 if (i > 0) else a * math.exp(i) for i in x]


def plot_elu():
    # param:起点，终点，间距
    x = np.arange(-6, 6, 0.1)
    sig = elu(x)
    print(sig)
    sig_der = elu_derivative(x)
    print(sig_der)

    plt.plot(x, sig)
    plt.plot(x, sig_der)
    plt.legend((u'elu', u'elu derivative'), loc='best')

    plt.savefig("activation_function2.png")
    plt.show()


if __name__ == '__main__':
    plot_elu()
