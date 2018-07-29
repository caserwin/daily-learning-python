# class A(object):
#     def __init__(self):
#         self.name = 'dicts: yidxue'
#         # self.age = 'dicts: 27'
#
#     def __getattr__(self, item):
#         if item == 'name':
#             return 'getattr: yidxue'
#         if item == 'age':
#             return 'getattr: 27'
#
#
# a = A()
# print(a.name)  # 从__dict__里获得的
# print(a.age)  # 从__getattr__获得的


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(self.name, age)
#
#
# p = Person("xueyiding", 24)  # 输出：xueyiding 24


class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __delattr__(self, *args, **kwargs):
        print('call func del attr')
        return object.__delattr__(self, *args, **kwargs)


a = A("yidxue", 27)
a.gender = "male"
print(a.__dict__)
del a.name
print(a.__dict__)
