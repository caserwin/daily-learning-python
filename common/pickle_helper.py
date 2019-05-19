#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/19 下午2:04
# @Author : Erwin
import pickle


def store_model(model, filename):
    fw = open(filename, 'wb')
    # 对象持久化包
    pickle.dump(model, fw)
    fw.close()


def read_model(filename):
    fr = open(filename, 'rb')
    print("load model {filename}".format(filename=filename))
    try:
        return pickle.load(fr, encoding='latin1')
    except:
        return pickle.load(fr)