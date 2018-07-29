# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 上午10:28
# @Author  : yidxue

import pandas as pd
import numpy as np

path = 'test.csv'
df = pd.read_csv(path, sep=',')

# ================ 查看数据特征 ================
# 查看数据类型
df.info()
# 查看字段名
print(df.columns.values)
# dataFrame 维度
print(df.shape)
# 查看前几条数据
print(df.head(10))
# 查看最后几条数据
print(df.tail())
# 数据概览
print(df.describe(include='all'))
# 查看一个字段缺失值情况
df['Browser'].isnull().sum()
# 查看每个字段缺失值情况
df.isnull().sum()
# 查看每行缺失值情况
df.isnull().sum(axis=1)
# 查看某列值的分布统计
df['Browser'].value_counts()
# 查看某列的取值
df['Browser'].unique()

# ================ 异常值处理 ================
# df['Browser'].hist()
# 异常值处理
for feature in df.columns:
    df.loc[df[feature] == -1, feature] = np.nan

# ================ 缺失值处理 ================
# 缺失值填充 - 对某列进行填充
df["OS"][df['MEI'].isnull()] = "0"

# 缺失值填充 - 众值填充
df.fillna(df.mode().iloc[0], inplace=True)

# 缺失值填充 - 中位数填充
df.fillna(df.median())

# ================ 规范化/正则化/ 处理 ================
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer

mmScaler = MinMaxScaler()  # 变换到[0,1]区间，也可以是其他固定大小的区间
ssScaler = StandardScaler()  # 0均值，单位方差
nScaler = Normalizer()  # 'l1', 'l2', or 'max', optional ('l2' by default)
# l2变换后，样本平方和1位. l1表示表示变换后，每个维度的绝对值之和为1

ssScaler.fit_transform(df['JMT'].values.reshape(-1, 1))
# 这是一种比较偷懒的写法，一般要先 fit 再执行 transform操作. 一般训练集和测试集同时执行 fit 操作， 然后在训练和测试阶段，分开进行transform操作。

# ================ 特征编码 ===================
dummy_df = pd.get_dummies(df, columns=['OS', 'Browser'], dummy_na=True)  # 获得哑变量
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from scipy import sparse

df['OS'] = LabelEncoder().fit_transform(df['OS'])
# TODO 这里有问题
# sparse.hstack((df, OneHotEncoder().fit_transform(df['OS'].reshape(-1, 1))))

# ================= 文本编码 ==================
from sklearn.feature_extraction.text import CountVectorizer

# ================= 连续特征离散化 ==================
from sklearn.preprocessing import Binarizer

# 已知值得区间
df['JMT'] = pd.cut(df['JMT'], bins=[0, 30, 50, 100, 200], labels=['a', 'b', 'c', 'd'], include_lowest=True).head(100)
a = LabelEncoder().fit_transform(df['JMT'])

# ===============  特征二值化 ===============


# ===============  评估函数 ===================
