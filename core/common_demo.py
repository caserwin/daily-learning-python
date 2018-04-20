ls =[]

ls.append("a")
print(ls)

print(4 % 2 == 0)
i=0
print(i+1)
#
a = [1, 2, 3, 4, 5]
b = [2, 2, 2, 0, 5]

# zip demo
c = [i + j for i, j in zip(a, b)]
print(c)

values = {"a", "b", "c"}
print(dict(zip(values, range(len(values)))))

# 三目运算符 demo
c = [0 if j == 0 else i / j for i, j in zip(a, b)]
print(c)

#
dict1 = {}
print(dict1 == {})

# 类型判断
dic = {"JOINMETHOD": {"ActiveX": "1", "Extension": {"USERTYPE": {"NEW": "1", "RETURN": "0"}}}}
print(isinstance(dic["JOINMETHOD"], dict))
print(dic["JOINMETHOD"])
print(dic)
