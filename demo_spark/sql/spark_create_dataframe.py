# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 上午10:41
# @Author  : yidxue
import pandas as pd
import datetime
import time
from component.demo_opentsdb.opentsdb_conn import OpenTSDBClient


def create_df(spark):
    df_pd = pd.DataFrame(
        data={'col1': [1, 2, 3],
              'col2': [-1.0, 0.5, 2.7],
              'col3': [[1, 2], [3, 4, 5], [6, 7, 8, 9]],
              'col4': ["text1", "text2 aa", "text3 cc"]}
    )
    return spark.createDataFrame(df_pd)


if __name__ == '__main__':
    # now_date = datetime.datetime.now().strftime("%Y-%m-%d") + " 00:00:00"
    now_date = "2019-05-03 00:00:00"
    pass_date = (datetime.datetime.now() + datetime.timedelta(days=-3)).strftime("%Y-%m-%d") + " 00:00:00"

    now_timestamp = int(time.mktime(time.strptime(now_date, '%Y-%m-%d %H:%M:%S')))
    pass_timestamp = int(time.mktime(time.strptime(pass_date, '%Y-%m-%d %H:%M:%S')))

    query_cond_dic = {
        "start": pass_timestamp,
        "end": now_timestamp,
        "queries": [
            {
                "aggregator": "none",
                "metric": "sys.error500.raw",
                "tags": {
                    "component": "meeting",
                    # "servertype": ,
                    "cluster": "AI",
                    # "errortype":
                }
            }
        ]
    }

    oc = OpenTSDBClient()
    raw_data = oc.get_data_by_post(query_cond_dic)

    print(raw_data)
