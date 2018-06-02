# plotly 画图示例

## 参考：<br>
[Filled Chord Diagram in Python](https://plot.ly/python/filled-chord-diagram/) <br>
[python应用plotly包实现和弦图chord diagram学习笔记（二)](http://c6h7ko2.blog.163.com/blog/static/2599780122016859504969)

## 步骤
1 先通过 pip install plotly 安装相关包。<br>
2 注册账号：https://plot.ly/ 。如果采用离线画图方式，则不用申请账号，下文有离线画图的代码<br>
3 在 https://plot.ly/settings/api#/ 拿到 API Key <br>
4 code 示例 <br>
&emsp;&emsp;4.1 在线画图demo:
```
import plotly
import plotly.figure_factory as ff
import plotly.plotly as py
plotly.tools.set_credentials_file(username='xxx', api_key='xxx')

data = [['', 'Emma', 'Isabella', 'Ava', 'Olivia', 'Sophia', 'row-sum'],
        ['Emma', 16, 3, 28, 0, 18, 65],
        ['Isabella', 18, 0, 12, 5, 29, 64],
        ['Ava', 9, 11, 17, 27, 0, 64],
        ['Olivia', 19, 0, 31, 11, 12, 73],
        ['Sophia', 23, 17, 10, 0, 34, 84]]

table = ff.create_table(data, index=True)
py.iplot(table, filename='Data-Table')
```
&emsp;&emsp;4.2离线画图demo:
```
import plotly
import plotly.figure_factory as ff

plotly.offline.init_notebook_mode(connected=True)

data = [['', 'Emma', 'Isabella', 'Ava', 'Olivia', 'Sophia', 'row-sum'],
        ['Emma', 16, 3, 28, 0, 18, 65],
        ['Isabella', 18, 0, 12, 5, 29, 64],
        ['Ava', 9, 11, 17, 27, 0, 64],
        ['Olivia', 19, 0, 31, 11, 12, 73],
        ['Sophia', 23, 17, 10, 0, 34, 84]]

table = ff.create_table(data, index=True)
plotly.offline.plot(table, filename='Data-Table')
  ```
5 输出：<br>

demo1 输出:
<div align=center><img width="500" height="200" src="https://github.com/caserwin/daily-learning-python/raw/master/pic/plotly_demo/chord_ diagram_1.png"/></div>
demo2 输出:
<div align=center><img width="450" height="450" src="https://github.com/caserwin/daily-learning-python/raw/master/pic/plotly_demo/chord_ diagram_2.png"/></div>
online_demo和offline_demo 输出:
<div align=center><img width="700" height="250" src="https://github.com/caserwin/daily-learning-python/raw/master/pic/plotly_demo/chord_ diagram_3.png"/></div>
