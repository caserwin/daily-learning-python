import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd

myfont = FontProperties(fname='/Library/Fonts/Songti.ttc')
plt.figure(figsize=(10, 4))

pds_mae = pd.Series({'CPSIm': 0.5562, 'cpc': 0.55884, 'pcc': 0.5581})
pds_mae.plot.bar()
plt.legend()
plt.show()
# pds_rmse = pd.Series({'CPSIm': 0.71466, 'cpc': 0.71342, 'pcc': 0.72004})
