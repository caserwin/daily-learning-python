import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd

myfont = FontProperties(fname='/Library/Fonts/Songti.ttc')

plt.figure(figsize=(10, 4))

cpcugu_series = pd.Series({
    10: 0.57183,
    20: 0.56407,
    30: 0.56022,
    40: 0.55821,
    50: 0.55708,
    60: 0.55802,
    70: 0.55435,
    80: 0.55594,
    90: 0.55595,
    100: 0.55575
})
cpcugu_series.plot(label='SF-H', marker='o')

cpc_series = pd.Series({
    10: 0.5725,
    20: 0.56399,
    30: 0.56164,
    40: 0.55829,
    50: 0.55884,
    60: 0.5588,
    70: 0.55686,
    80: 0.55855,
    90: 0.55853,
    100: 0.55902
})
cpc_series.plot(label='CPSim', marker='^')

pcc_series = pd.Series({
    10: 0.57359,
    20: 0.5629,
    30: 0.56281,
    40: 0.55929,
    50: 0.55899,
    60: 0.5588,
    70: 0.55967,
    80: 0.559,
    90: 0.55858,
    100: 0.5579
})
pcc_series.plot(label='PCC', marker='s')

# pmf_series = pd.Series({
#     '10': 0.7204,
#     '20': 0.7198,
#     '30': 0.6321,
#     '40': 0.6319,
#     '50': 0.6211,
#     '60': 0.601,
#     '70': 0.632,
#     '80': 0.5812,
#     '90': 0.6511,
#     '100': 0.671
# })
# pmf_series.plot(label='pmf')
#
# smf_series = pd.Series({
#     '10': 0.7392,
#     '20': 0.7192,
#     '30': 0.6431,
#     '40': 0.6313,
#     '50': 0.6122,
#     '60': 0.6002,
#     '70': 0.5695,
#     '80': 0.5815,
#     '90': 0.6102,
#     '100': 0.5995
# })
# smf_series.plot(label='smf')


CMF_series = pd.Series({
    10: 0.5745,
    20: 0.5660,
    30: 0.5645,
    40: 0.5627,
    50: 0.5601,
    60: 0.5590,
    70: 0.5572,
    80: 0.5587,
    90: 0.5579,
    100: 0.5580
})
CMF_series.plot(label='CMF', marker='+')

HeteMF_series = pd.Series({
    10: 0.5772,
    20: 0.5706,
    30: 0.5675,
    40: 0.5640,
    50: 0.5621,
    60: 0.5615,
    70: 0.5600,
    80: 0.5588,
    90: 0.5574,
    100: 0.5578
})
HeteMF_series.plot(label='HeteMF', marker='*')

plt.title("douban MAE")
plt.ylabel("MAE")
plt.xlabel("k-neighbors")
plt.legend()
plt.show()
