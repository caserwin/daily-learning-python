#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 13:30
# @Author  : erwin
import pandas as pd

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

month_df = pd.read_csv("./monthly.csv", sep=',')
# print(month_df.head())

week_df = pd.read_csv("./weekly.csv", sep=',')
# print(week_df.head())

# 聚合
tmp_month_gp_df = month_df.groupby(['MONTHID', 'HOSTID'])
tmp_week_gp_df = week_df.groupby(['WEEKID', 'HOSTID'])

month_res_df = pd.concat([
    tmp_month_gp_df['USERID'].min(),
    tmp_month_gp_df['MAX_DURATION'].max(),
    tmp_month_gp_df['MIN_DURATION'].min(),
    tmp_month_gp_df['MAX_TOTAL_ATTENDEE'].max(),
    tmp_month_gp_df['MIN_TOTAL_ATTENDEE'].min(),
    tmp_month_gp_df['MONTHLY_TOTAL_DURATION'].sum(),
    tmp_month_gp_df['MONTHLY_TOTAL_ATTENDEE'].sum(),
    tmp_month_gp_df['MONTHLY_TOTAL_INVITED'].sum(),
    tmp_month_gp_df['MONTHLY_TOTAL_MTG'].sum()
], axis=1)

week_res_df = pd.concat([
    tmp_week_gp_df['USERID'].min(),
    tmp_week_gp_df['MAX_DURATION'].max(),
    tmp_week_gp_df['MIN_DURATION'].min(),
    tmp_week_gp_df['MAX_TOTAL_ATTENDEE'].max(),
    tmp_week_gp_df['MIN_TOTAL_ATTENDEE'].min(),
    tmp_week_gp_df['WEEKLY_TOTAL_DURATION'].sum(),
    tmp_week_gp_df['WEEKLY_TOTAL_ATTENDEE'].sum(),
    tmp_week_gp_df['WEEKLY_TOTAL_INVITED'].sum(),
    tmp_week_gp_df['WEEKLY_TOTAL_MTG'].sum()
], axis=1)

month_dict_AVG_DURATION = {}
for index, row in month_df.iterrows():
    key = str(row["MONTHID"]) + "_" + str(row["HOSTID"])
    if key not in month_dict_AVG_DURATION.keys():
        month_dict_AVG_DURATION[key] = [int(row["AVG_DURATION"]) * int(row["MONTHLY_TOTAL_MTG"]),
                                        int(row["MONTHLY_TOTAL_MTG"])]
    else:
        month_dict_AVG_DURATION[key][0] = month_dict_AVG_DURATION[key][0] + int(row["AVG_DURATION"]) * int(
            row["MONTHLY_TOTAL_MTG"])
        month_dict_AVG_DURATION[key][1] = month_dict_AVG_DURATION[key][1] + int(row["MONTHLY_TOTAL_MTG"])

month_dict_AVG_DURATION_res = [[item[0].split('_')[0], item[0].split('_')[1], round(item[1][0] / item[1][1], 2)] for
                               item in month_dict_AVG_DURATION.items()]
month_df1 = pd.DataFrame(data=month_dict_AVG_DURATION_res, columns=["MONTHID", "HOSTID", "AVG_DURATION"])

week_dict_AVG_DURATION = {}
for index, row in week_df.iterrows():
    key = str(row["WEEKID"]) + "_" + str(row["HOSTID"])
    if key not in week_dict_AVG_DURATION.keys():
        week_dict_AVG_DURATION[key] = [int(row["AVG_DURATION"]) * int(row["WEEKLY_TOTAL_MTG"]),
                                       int(row["WEEKLY_TOTAL_MTG"])]
    else:
        week_dict_AVG_DURATION[key][0] = week_dict_AVG_DURATION[key][0] + int(row["AVG_DURATION"]) * int(
            row["WEEKLY_TOTAL_MTG"])
        week_dict_AVG_DURATION[key][1] = week_dict_AVG_DURATION[key][1] + int(row["WEEKLY_TOTAL_MTG"])

week_dict_AVG_DURATION_res = [[item[0].split('_')[0], item[0].split('_')[1], round(item[1][0] / item[1][1], 2)] for
                              item in week_dict_AVG_DURATION.items()]
week_df1 = pd.DataFrame(data=week_dict_AVG_DURATION_res, columns=["WEEKID", "HOSTID", "AVG_DURATION"])

month_dict_AVG_TOTAL_ATTENDEE = {}
for index, row in month_df.iterrows():
    key = str(row["MONTHID"]) + "_" + str(row["HOSTID"])
    if key not in month_dict_AVG_TOTAL_ATTENDEE.keys():
        month_dict_AVG_TOTAL_ATTENDEE[key] = [int(row["AVG_TOTAL_ATTENDEE"]) * int(row["MONTHLY_TOTAL_MTG"]),
                                              int(row["MONTHLY_TOTAL_MTG"])]
    else:
        month_dict_AVG_TOTAL_ATTENDEE[key][0] = month_dict_AVG_TOTAL_ATTENDEE[key][0] + int(
            row["AVG_TOTAL_ATTENDEE"]) * int(row["MONTHLY_TOTAL_MTG"])
        month_dict_AVG_TOTAL_ATTENDEE[key][1] = month_dict_AVG_TOTAL_ATTENDEE[key][1] + int(row["MONTHLY_TOTAL_MTG"])

month_dict_AVG_TOTAL_ATTENDEE_res = [
    [item[0].split('_')[0], item[0].split('_')[1], round(item[1][0] / item[1][1], 2)] for
    item in month_dict_AVG_TOTAL_ATTENDEE.items()]
month_df2 = pd.DataFrame(data=month_dict_AVG_TOTAL_ATTENDEE_res, columns=["MONTHID", "HOSTID", "AVG_TOTAL_ATTENDEE"])

week_dict_AVG_TOTAL_ATTENDEE = {}
for index, row in week_df.iterrows():
    key = str(row["WEEKID"]) + "_" + str(row["HOSTID"])
    if key not in week_dict_AVG_TOTAL_ATTENDEE.keys():
        week_dict_AVG_TOTAL_ATTENDEE[key] = [int(row["AVG_TOTAL_ATTENDEE"]) * int(row["WEEKLY_TOTAL_MTG"]),
                                             int(row["WEEKLY_TOTAL_MTG"])]
    else:
        week_dict_AVG_TOTAL_ATTENDEE[key][0] = week_dict_AVG_TOTAL_ATTENDEE[key][0] + int(
            row["AVG_TOTAL_ATTENDEE"]) * int(row["WEEKLY_TOTAL_MTG"])
        week_dict_AVG_TOTAL_ATTENDEE[key][1] = week_dict_AVG_TOTAL_ATTENDEE[key][1] + int(row["WEEKLY_TOTAL_MTG"])

week_dict_AVG_TOTAL_ATTENDEE_res = [
    [item[0].split('_')[0], item[0].split('_')[1], round(item[1][0] / item[1][1], 2)] for
    item in week_dict_AVG_TOTAL_ATTENDEE.items()]
week_df2 = pd.DataFrame(data=week_dict_AVG_TOTAL_ATTENDEE_res, columns=["WEEKID", "HOSTID", "AVG_TOTAL_ATTENDEE"])

month_df1.MONTHID = month_df1.MONTHID.astype(int)
month_df1.HOSTID = month_df1.HOSTID.astype(int)
month_df2.MONTHID = month_df2.MONTHID.astype(int)
month_df2.HOSTID = month_df2.HOSTID.astype(int)

week_df1.WEEKID = week_df1.WEEKID.astype(int)
week_df1.HOSTID = week_df1.HOSTID.astype(int)
week_df2.WEEKID = week_df2.WEEKID.astype(int)
week_df2.HOSTID = week_df2.HOSTID.astype(int)

m_df = month_res_df.merge(month_df1, how='inner', on=['MONTHID', 'HOSTID']).merge(month_df2, how='inner',
                                                                                  on=['MONTHID', 'HOSTID'])

w_df = week_res_df.merge(week_df1, how='inner', on=['WEEKID', 'HOSTID']).merge(week_df2, how='inner',
                                                                               on=['WEEKID', 'HOSTID'])

m_df.sort_values(by=['HOSTID', 'MONTHID']).to_csv("~/month.csv", sep=",", index=False, header=True)
w_df.sort_values(by=['HOSTID', 'WEEKID']).to_csv("~/week.csv", sep=",", index=False, header=True)
