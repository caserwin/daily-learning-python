# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 上午10:45
# @Author  : yidxue

import plotly
import plotly.figure_factory as ff
import plotly.plotly as py

plotly.tools.set_credentials_file(username='xxx12345', api_key='xSsbpWPijxA5ROFgprsM')

data = [['', 'Emma', 'Isabella', 'Ava', 'Olivia', 'Sophia', 'row-sum'],
        ['Emma', 16, 3, 28, 0, 18, 65],
        ['Isabella', 18, 0, 12, 5, 29, 64],
        ['Ava', 9, 11, 17, 27, 0, 64],
        ['Olivia', 19, 0, 31, 11, 12, 73],
        ['Sophia', 23, 17, 10, 0, 34, 84]]

table = ff.create_table(data, index=True)
py.iplot(table, filename='Data-Table')
