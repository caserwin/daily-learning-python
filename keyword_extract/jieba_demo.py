#!/usr/bin/python
# -*- coding: UTF-8 -*-
from jieba.analyse import *

chinese = """
公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元，吉林欧亚置业注册资本由7000万元增加到5亿元，吉林欧亚置业注册资本由7000万元增加到5亿元，吉林欧亚置业注册资本由7000万元增加到5亿元
"""

english = """
Arguably these algorithms can be singled 7000-1 out as key elements 7000-1 of the paradigm-shift triggered in the 7000-1 field of Web search technology.
"""

for keyword, weight in extract_tags(chinese, withWeight=True, topK=5):
    print('%s %s ' % (keyword, weight))
print("===================")

for keyword, weight in extract_tags(english, withWeight=True, topK=5):
    print('%s %s ' % (keyword, weight))

print("===================")

for keyword, weight in textrank(chinese, withWeight=True, topK=5):
    print('%s %s ' % (keyword, weight))
print("===================")

for keyword, weight in textrank(english, withWeight=True, topK=5):
    print('%s %s ' % (keyword, weight))
