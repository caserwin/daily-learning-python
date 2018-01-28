# coding:utf-8
# 拉格朗日插值代码
import pandas as pd  # 导入数据分析库Pandas
from scipy.interpolate import lagrange  # 导入拉格朗日插值函数

# 构建原始数据
data = pd.DataFrame([
    ["2015/3/1", 59],
    ["2015/2/28", 2618.2],
    ["2015/2/27", 2608.4],
    ["2015/2/26", 2651.9],
    ["2015/2/25", 3442.1],
    ["2015/2/24", 3393.1],
    ["2015/2/23", 3136.6],
    ["2015/2/22", 3744.1],
    ["2015/2/21", ],
    ["2015/2/20", 4060.3],
    ["2015/2/19", 3614.7],
    ["2015/2/18", 3295.5],
    ["2015/2/16", 2332.1],
    ["2015/2/15", 2699.3],
    ["2015/2/14", ],
    ["2015/2/13", 3036.8],
    ["2015/2/12", 1865],
    ["2015/2/11", 3014.3],
    ["2015/2/10", 2742.8],
    ["2015/2/9", 2173.5],
    ["2015/2/8", 3161.8],
    ["2015/2/7", 3023.8],
    ["2015/2/6", 2998.1],
], columns=[u'日期', u'销量'])

# 设置异常值,把销量大于5000和销量小于400的异常值替换为None
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None

# 把要处理的数据取出来,pandas中dataframe格式单独取出一列就是series数据格式
tmp_data_1 = data[u'销量'].copy()
tmp_data_2 = data[u'销量'].copy()


def ployinterp_column(series, pos, window=5):
    """
    :param series: 列向量
    :param pos: 被插值的位置
    :param window: 为取前后的数据个数
    :return:
    """
    y = series[list(range(pos - window, pos)) + list(range(pos + 1, pos + 1 + window))]  # 取数
    y = y[y.notnull()]  # 剔除空值
    return lagrange(y.index, list(y))(pos)  # 插值并返回插值结果


def sma_mothod(series, pos, window=5):
    """
    :param series: 列向量
    :param pos: 被插值的位置
    :param window: 为取前后的数据个数
    :return:
    """
    y = series[list(range(pos - window, pos)) + list(range(pos + 1, pos + 1 + window))]  # 取数
    y = y[y.notnull()]
    return reduce(lambda a, b: a + b, y) / len(y)

for j in range(len(tmp_data_1)):
    if (tmp_data_1.isnull())[j]:  # 如果为空即插值。
        tmp_data_1[j] = ployinterp_column(tmp_data_1, j)
        print j, data.loc[j, u'日期'], tmp_data_1[j]

print

for j in range(len(tmp_data_2)):
    if (tmp_data_2.isnull())[j]:  # 如果为空即插值。
        tmp_data_2[j] = sma_mothod(tmp_data_2, j)
        print j, data.loc[j, u'日期'], tmp_data_2[j]