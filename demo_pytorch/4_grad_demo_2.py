# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 上午10:44
# @Author  : yidxue

import torch

# x = torch.ones(2, 2, requires_grad=True)
x = torch.tensor([[1, 2], [3, 4]], requires_grad=True, dtype=torch.float)
print(x)
y = x + 2
print(y)
print(y.grad_fn)
z = y * y * 3
out = z.sum()
print(z)
print(out)

# # .requires_grad_( ... ) changes an existing Tensor’s requires_grad flag in-place. The input flag defaults to False if not given.
# print("\nrequires_grad_ demo")
# a = torch.randn(2, 2)
# print(a)
# a = ((a * 3) / (a - 1))
# print(a)
# print(a.requires_grad)
# a.requires_grad_(True)
# print(a.requires_grad)
# b = (a * a).sum()
# print(b)
# print(b.grad_fn)

# GRADIENTS
out.backward()
print(x.grad)

# Jacobian-vector product
print("\nJacobian-vector product")
x = torch.randn(3, requires_grad=True)
y = x * 2
print(x)
print(y)
while y.data.norm() < 1000:
    y = y * 2

print(y)

v = torch.tensor([3.0, 3.0, 3.0], dtype=torch.float)
y.backward(v)

print(x.grad)
