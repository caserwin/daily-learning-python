# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午3:20
# @Author  : yidxue


def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton
