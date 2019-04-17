# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 下午8:01
# @Author  : yidxue
import torch
import numpy as np
# 随机初始化 10 * 3 矩阵，其中数值符合0-1正太分布
x = torch.randn(5, 3)
print(x)
# print(torch.randn(4))

# 0-1正太分布，维度和xxian相同
print(torch.randn_like(x, dtype=torch.float))

# 随机初始化 10 * 3 矩阵，其中数值符合0-1均匀分布
x = torch.rand(5, 3)
print(x)
# print(torch.rand(4))

x = torch.tensor([5.5, 3])
print(x)

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

x = torch.ones(5, 3, dtype=torch.long)
print(x)

# 把numpy 转化为tensor
a = np.ones(5)
print(torch.from_numpy(a))
