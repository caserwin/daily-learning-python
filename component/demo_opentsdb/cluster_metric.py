#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-22 17:45
# @Author  : erwin
import datetime
import time
import pandas as pd
from component.demo_opentsdb.opentsdb_conn import OpenTSDBClient
from machine_learning.similarity.dtw.hierarchical_helper import HierarchicalHelper
from common.pickle_helper import store_model

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)


def customizedStandardize(df, startIndex):
    temp = df.reset_index()
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(temp.iloc[:, range(startIndex, temp.columns.size)])
    data = pd.DataFrame(scaler.transform(temp.iloc[:, range(startIndex, temp.columns.size)]))
    return pd.DataFrame(data.values, columns=df.columns[startIndex - 1:len(df.columns)], index=df.index)


def modeling(df):
    from dtaidistance import dtw
    import numpy as np
    series = np.matrix(df.T)
    dist_matrix = dtw.distance_matrix_fast(series)
    from dtaidistance import clustering
    model3 = clustering.LinkageTree(dtw.distance_matrix_fast, {})
    model3.fit(series)
    return dist_matrix, model3


if __name__ == '__main__':
    train_day = 1
    now_date = datetime.datetime.now().strftime("%Y-%m-%d") + " 00:00:00"
    pass_date = (datetime.datetime.now() + datetime.timedelta(days=-train_day)).strftime("%Y-%m-%d") + " 00:00:00"

    now_timestamp = int(time.mktime(time.strptime(now_date, '%Y-%m-%d %H:%M:%S')))
    pass_timestamp = int(time.mktime(time.strptime(pass_date, '%Y-%m-%d %H:%M:%S')))

    # B A L R
    cluster_name = "ALL"
    query_cond_dic = {
        "start": pass_timestamp,
        "end": now_timestamp,
        "queries": [
            {
                "aggregator": "none",
                "metric": "sys.error500.raw",
                "tags": {
                    # "cluster": cluster_name,
                }
            }
        ]
    }

    oc = OpenTSDBClient()
    raw_datas = oc.get_data_by_post_all(query_cond_dic)

    # OpenTSDB 数据转成 Pandas DataFrame
    records = {data.get("tags").get("cluster") + "_" + data.get("tags").get("errortype"): data.get("dps") for data in
               raw_datas}

    clusterAll = pd.DataFrame(data=records).fillna(0)
    clusterAllStd = customizedStandardize(clusterAll, 1)
    dist_matrix, model = modeling(clusterAllStd)

    col_name = clusterAll.columns.values
    tree_helper = HierarchicalHelper(model, dist_matrix, col_name)

    store_model(tree_helper, "./tree_helper.model")
