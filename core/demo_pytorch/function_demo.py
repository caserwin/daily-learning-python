# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 下午2:04
# @Author  : yidxue
import torch

x = torch.tensor([2, 2, 2, 2], requires_grad=True, dtype=torch.float)
# x = torch.FloatTensor([2, 2, 2, 2])
print(x.data)
print(x.data.norm())

y = torch.tensor(2, requires_grad=True, dtype=torch.float)
print(y.item())
print(y.data.norm())

# clamp 函数
N, D_in, H = 10, 4, 6
device = torch.device('cpu')

x = torch.randn(N, D_in, device=device)
w1 = torch.randn(D_in, H, device=device)

h = x.mm(w1)
## min 参数表示一个tensor中的元素最小是多少，也就是说把小于 min的数都设为 min。max 参数表示一个tensor中的元素最大是多少，也就是说把大于 max的数都设为 max
h_relu = h.clamp(max=1)

print(h)
print(h_relu)
