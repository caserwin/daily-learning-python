# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import numpy as np
import pandas as pd

# 基于numpy 构建
date_index = pd.date_range('20140729', periods=10)
print(pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'], index=date_index))
print("=" * 20)

# 基于list构建，其实这里也可以不需要 numpy.
data = np.array([[1, 2, 3, 4],
                 [4, 5, 6, 8],
                 [2, 3, 5, 9]])
index = ['a', 'b', 'c']
columns = ['A', 'B', 'C', 'D']
print(pd.DataFrame(data=data, index=index, columns=columns))
print("=" * 20)

# 基于列表-字典类型
dic_ls = [{'col1': 'a', 'col2': '1'}, {'col1': 'b', 'col2': '2'}]
print(pd.DataFrame(data=dic_ls))
print("=" * 20)

# 基于字典-列表类型
df = pd.DataFrame(data={'columns1': ['a', 'b', 'c'], 'columns2': ['c', 'd', 'e']})
print(df)
print("=" * 20)

# 基于json字符串
print(pd.read_json("""[{"col1": "a", "col2": "1"}, {"col1": "b", "col2": "2"}]"""))
print(pd.read_json('./data/test.json'))