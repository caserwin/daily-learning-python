# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [4, 5, 6]})
print(df)
print(df.dtypes)
print("=" * 20)

# 字段重命名
print(df.rename(index=str, columns={"A": "a", "B": "b"}))
print("=" * 20)

# 字段重命名
df.columns = ['C', 'D', 'E']
print(df)
print("=" * 20)

# index 重命名：dataframe.rename()


# index
print(df.reset_index())
print("=" * 20)

# 输出字段名
print(df.columns.values)
print("=" * 20)

# 类型转换
df[['C', 'D']] = df[['C', 'D']].astype(float)
df.E = df.E.astype(str)
print(df.dtypes)
