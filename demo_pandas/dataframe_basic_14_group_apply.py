import pandas as pd
from pandas import *

from common.util_function import *

"""
参考：https://stackoverflow.com/questions/14529838/apply-multiple-functions-to-multiple-groupby-columns
"""

# np.random.seed(1)

df = pd.DataFrame(np.random.rand(8, 4), columns=list('abcd'))
df['group'] = [0, 0, 1, 1, 0, 2, 1, 1]

print(df)

print_line("apply 方法1 -- 传入dict，转Pandas Series")


def f(x):
    # 这里 x 是分组后的每个 dataframe
    d = {'a_sum': x['a'].sum(), 'a_max': x['a'].max(), 'b_mean': x[x['b'] > 0.5]['b'].mean(),
         'c_d_prodsum': (x['c'] * x['d']).sum()}
    return pd.Series(d, index=['a_sum', 'a_max', 'b_mean', 'c_d_prodsum'])


print(df.groupby('group').apply(f))

print_line("apply 方法2 -- 传入list，转Pandas Series")


def f_mi(x):
    d = [x['a'].sum(), x['a'].max(), x['b'].mean(), (x['c'] * x['d']).sum()]
    return pd.Series(d, index=['a_sum', 'a_max', 'b_mean', 'c_d_prodsum'])


print(df.groupby('group').apply(f_mi))

print_line("apply 方法3 -- 暂时不清楚 df.a.groupby(list) 形式的apply 以上两种写法怎么实现")
print(df.a.groupby(df['group']).apply(lambda x: x.count()))
