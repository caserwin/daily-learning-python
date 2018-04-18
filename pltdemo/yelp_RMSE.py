import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd

myfont = FontProperties(fname='/Library/Fonts/Songti.ttc')

plt.figure(figsize=(10, 4))

cpcugu_series = pd.Series({
    10: 1.116654,
    20: 1.103245,
    30: 1.10383,
    40: 1.102918,
    50: 1.096491,
    60: 1.09457,
    70: 1.09945,
    80: 1.099613,
    90: 1.100597,
    100: 1.098
})
cpcugu_series.plot(label='SF-H', marker='o')

cpc_series = pd.Series({
    10: 1.118507,
    20: 1.106035,
    30: 1.106813,
    40: 1.108985,
    50: 1.102323,
    60: 1.099561,
    70: 1.100729,
    80: 1.104909,
    90: 1.104872,
    100: 1.101328
})
cpc_series.plot(label='CPSim', marker='^')

pcc_series = pd.Series({
    10: 1.129643,
    20: 1.127187,
    30: 1.121845,
    40: 1.12173,
    50: 1.126221,
    60: 1.121505,
    70: 1.122001,
    80: 1.120009,
    90: 1.11501,
    100: 1.114502
})
pcc_series.plot(label='PCC', marker='s')

CMF_series = pd.Series({
    10: 1.124,
    20: 1.110,
    30: 1.1128,
    40: 1.117,
    50: 1.1194,
    60: 1.1172,
    70: 1.1095,
    80: 1.1071,
    90: 1.10801,
    100: 1.1064
})
CMF_series.plot(label='CMF', marker='+')

HeteMF_series = pd.Series({
    10: 1.125507,
    20: 1.114035,
    30: 1.11,
    40: 1.113985,
    50: 1.111323,
    60: 1.104561,
    70: 1.103729,
    80: 1.10209,
    90: 1.101872,
    100: 1.1
})
HeteMF_series.plot(label='HeteMF', marker='*')

plt.title("yelp RMSE")
plt.ylabel("RMSE")
plt.xlabel("k-neighbors")
plt.legend()
plt.show()
