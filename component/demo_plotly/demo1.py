# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 上午10:40
# @Author  : yidxue

import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)

data = dict(type='choropleth',
            locations=['AZ', 'CA', 'NY'],
            locationmode='USA-states',
            colorscale='Portland',
            text=['text1', 'text2', 'text3'],
            z=[1.0, 2.0, 3.0],
            colorbar={'title': 'Colorbar Title'})

layout = dict(geo={'scope': 'usa'})
choromap = go.Figure(data=[data], layout=layout)
plotly.offline.plot(choromap)
