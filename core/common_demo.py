# -*- coding: utf-8 -*-

if __name__ == '__main__':
    '''
    三目运算符
    '''
    print(True if 5 > 3 else False)

    '''
    类型判断
    '''
    dic = {"JOINMETHOD": {"ActiveX": "1", "Extension": {"USERTYPE": {"NEW": "1", "RETURN": "0"}}}}
    print(isinstance(dic["JOINMETHOD"], dict))
    print(isinstance([1, 2, 3], list))

    '''
    all() 函数使用示例，通常用于参数校验
    '''
    print(all([0, 1, 2, 3, 4]))
    print(all([1, 2, 3, ""]))
    print(all([1, 2, 3, None]))
    print(all([1, 2, 3, False]))
    print(all([1, 2, 3, 4]))

    '''
    python 随机函数random模块
    choice() : 对于一个可迭代的对象，从中随机选出一个值。
    shuffle() : 对于一个可迭代的对象，进行混洗。
    uniform() : 随机生成小数
    '''
    import random

    ls = [1, 2, 3, 4, 5]
    random.shuffle(ls)
    print(ls)
    print(random.choice(ls))
    print(random.uniform(10, 20))  # python 生成 10 - 20之间的随机小数

    '''
    range 用法
    '''
    print(range(5, -1, -2))
    print(range(5, -1, -1))
    print(range(1, 5, 1))
    print(range(1, 5, 2))
