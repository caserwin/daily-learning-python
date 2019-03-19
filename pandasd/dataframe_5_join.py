# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午2:36
# @Author  : yidxue
import pandas as pd

df1 = pd.DataFrame(data={'name': ['a', 'b', 'c', 'd'], 'gender': ['male', 'male', 'female', 'female']})

df2 = pd.DataFrame(data={'name': ['a', 'b', 'c', 'e'], 'age': [21, 22, 23, 20]})

# inner join
print("=" * 10 + "inner join" + "=" * 10)
print(pd.merge(df1, df2, on=['name'], how='inner'))

# inner join
print()
print(df1.merge(df2, how='inner', on=['name']))

# left join
print("=" * 10 + "left join" + "=" * 10)
print(pd.merge(df1, df2, on=['name'], how='left'))

# outer join
print("=" * 10 + "outer join" + "=" * 10)
print(pd.merge(df1, df2, on=['name'], how='outer'))
