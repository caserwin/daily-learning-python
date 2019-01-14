# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 下午8:17
# @Author  : yidxue
import torch

# 加法示例，建议多试试x,y 维度不同的情况，摸索下
x = torch.rand(1, 3)
y = torch.rand(2, 3)
print(x)
print(y)
print(x + y)

print(torch.add(x, y))

# 取出其中一行
print(y[0])

# 加一
print(y[0].add_(1))  # 需要注意，这么操作后，原来的y也会变了，相当于引用传递。
print(y)

# 转化为 numpy
print(y[0].numpy())

print("=" * 40)
# 在cuda上运行
if torch.cuda.is_available():
    print("cuda calculate")
    device = torch.device("cuda")  # a CUDA device object
    y = torch.ones_like(x, device=device)  # directly create a tensor on GPU
    x = x.to(device)  # or just use strings ``.to("cuda")``
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))  # ``.to`` can also change dtype together!
