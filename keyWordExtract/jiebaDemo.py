#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jieba

strt = "人人编程时我们，适合编程初学者学习python的教材，也是好专业的童鞋关注学习"
# 全模式
sl = jieba.cut(strt, cut_all=True)
print "全模式分词结果:", ",".join(sl)
print('\n')

# 精确模式,默认hi精确模式，所以可以不指定cut_all=False
sl = jieba.cut(strt, cut_all=False)
print "精确模式分词结果:", ",".join(sl)
print('\n')

# 搜索引擎模式
sl = jieba.cut_for_search(strt)
print "搜索引擎模式分词结果:", ",".join(sl)
