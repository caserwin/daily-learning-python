#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-15 10:22
# @Author  : erwin
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def customizedStandardize(df, startIndex):
    temp = df.reset_index()
    scaler = StandardScaler()
    scaler.fit(temp.iloc[:, range(startIndex, temp.columns.size)])
    data = pd.DataFrame(scaler.transform(temp.iloc[:, range(startIndex, temp.columns.size)]))
    return pd.DataFrame(data.values, columns=df.columns[startIndex - 1:len(df.columns)], index=df.index)


if __name__ == '__main__':
    data = np.array([[0, 0, 0, 1],
                     [0, 1, 0, 2],
                     [1, 2, 1, 1],
                     [2, 0, 2, 2],
                     [1, 0, 1, 1],
                     [0, 0, 0, 2],
                     [1, 0, 0, 1],
                     [0, 0, 10, 2]])

    df = pd.DataFrame(data=data, dtype=float)

    print(df)
    clusterPivotStd1 = customizedStandardize(df, 1)
    print(clusterPivotStd1)

    clusterPivotStd1 = customizedStandardize(df, 2)
    print(clusterPivotStd1)
