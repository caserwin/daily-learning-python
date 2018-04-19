a = [1, 2, 3, 4, 5]
b = [2, 2, 2, 0, 5]

# zip demo
c = [i + j for i, j in zip(a, b)]
print(c)

# 三目运算符 demo
c = [0 if j == 0 else i / j for i, j in zip(a, b)]
print(c)
