import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd

myfont = FontProperties(fname='/Library/Fonts/Songti.ttc')

plt.figure(figsize=(10, 4))

cpcugu_series = pd.Series({
    10: 0.857232,
    20: 0.84854,
    30: 0.848683,
    40: 0.847211,
    50: 0.842211,
    60: 0.845398,
    70: 0.843259,
    80: 0.844101,
    90: 0.847134,
    100: 0.853053
})
cpcugu_series.plot(label='CPSim', marker='o')


cpc_series = pd.Series({
    10: 0.858582,
    20: 0.84991,
    30: 0.849614,
    40: 0.852794,
    50: 0.845739,
    60: 0.844346,
    70: 0.845175,
    80: 0.850605,
    90: 0.848854,
    100: 0.847123
})
cpc_series.plot(label='CPC', marker='^')


pcc_series = pd.Series({
    10: 0.87809,
    20: 0.878505,
    30: 0.880258,
    40: 0.880353,
    50: 0.882304,
    60: 0.878781,
    70: 0.880575,
    80: 0.87337,
    90: 0.866951,
    100: 0.865995
})
pcc_series.plot(label='PCC', marker='s')

CMF_series = pd.Series({
    10: 0.8849,
    20: 0.88005,
    30: 0.878258,
    40: 0.87453,
    50: 0.872304,
    60: 0.874781,
    70: 0.87226,
    80: 0.8641,
    90: 0.862951,
    100: 0.862695
})
CMF_series.plot(label='CMF', marker='+')

HeteMF_series = pd.Series({
    10: 0.8872,
    20: 0.88,
    30: 0.8762,
    40: 0.8752,
    50: 0.8742,
    60: 0.8754,
    70: 0.87426,
    80: 0.8661,
    90: 0.86513,
    100: 0.8640
})
HeteMF_series.plot(label='HeteMF', marker='*')

plt.title("yelp MAE")
plt.ylabel("MAE")
plt.xlabel("k-neighbors")
plt.legend()
plt.show()
