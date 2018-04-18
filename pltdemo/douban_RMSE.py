import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd

myfont = FontProperties(fname='/Library/Fonts/Songti.ttc')

plt.figure(figsize=(10, 4))

cpcugu_series = pd.Series({
    10: 0.73382,
    20: 0.72378,
    30: 0.72045,
    40: 0.71644,
    50: 0.71714,
    60: 0.71624,
    70: 0.71124,
    80: 0.7137,
    90: 0.71754,
    100: 0.7169
})
cpcugu_series.plot(label='SF-H', marker='o')


cpc_series = pd.Series({
    10: 0.73468,
    20: 0.72431,
    30: 0.72111,
    40: 0.71712,
    50: 0.71342,
    60: 0.71832,
    70: 0.71439,
    80: 0.71699,
    90: 0.71776,
    100: 0.71678
})
cpc_series.plot(label='CPSim', marker='^')


pcc_series = pd.Series({
    10: 0.7425,
    20: 0.72797,
    30: 0.72646,
    40: 0.72195,
    50: 0.72004,
    60: 0.72397,
    70: 0.72129,
    80: 0.72012,
    90: 0.71976,
    100: 0.71936
})
pcc_series.plot(label='PCC', marker='s')

CMF_series = pd.Series({
    10: 0.7495,
    20: 0.7326,
    30: 0.7275,
    40: 0.7248,
    50: 0.7245,
    60: 0.7239,
    70: 0.7232,
    80: 0.7212,
    90: 0.72,
    100: 0.719
})
CMF_series.plot(label='CMF', marker='+')

HeteMF_series = pd.Series({
    10: 0.7438,
    20: 0.7338,
    30: 0.7305,
    40: 0.7264,
    50: 0.7271,
    60: 0.7262,
    70: 0.7212,
    80: 0.7237,
    90: 0.7275,
    100: 0.727
})
HeteMF_series.plot(label='HeteMF', marker='*')

plt.title("douban RMSE")
plt.ylabel("RMSE")
plt.xlabel("k-neighbors")
plt.legend()
plt.show()
