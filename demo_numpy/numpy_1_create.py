# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 下午5:54
# @Author  : yidxue
import numpy as np
from demo_pandas.function.util_function import *
np.set_printoptions(precision=3)

print_line("array to list")
print_br(np.array([1, 2, 3]))
print_br(np.array([(1, 2, 3), (4, 5, 6)]))

print_line("numpy matrix with fixed-step")
print_br(np.linspace(0, 100, 10).reshape((5, 2)))
print_br(np.arange(0, 100, 10).reshape((5, 2)))

print_line("numpy array with fixed-step")
print_br(np.linspace(0, 100, 8))
print_br(np.arange(0, 100, 3))

print_line("numpy full function")
print_br(np.full((2, 3), np.inf))
print_br(np.full((2, 3), 0))

print_line("numpy with all values 0")
print_br(np.zeros(3))
print_br(np.zeros((3, 2)))

print_line("numpy with all values 1")
print_br(np.ones(3))
print_br(np.ones((3, 4)))

print_line("numpy random create 3x4 array")
print_br(np.random.rand(3, 4))
print_br(np.random.rand(3, 4) * 100)
print_br(np.random.randint(5, size=(3, 4)))

print_line("5x5 array of 0 with 1 on diagonal")
print_br(np.eye(5))
