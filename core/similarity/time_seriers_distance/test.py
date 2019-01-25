import logging
import pandas as pd

logging.getLogger('fbprophet').setLevel(logging.ERROR)
import warnings

warnings.filterwarnings("ignore")
from dtaidistance import dtw_visualisation as dtwvis
from dtaidistance import dtw
import numpy as np

dfStandardizedJMT = pd.read_csv("dfStandardizedJMT.csv")
series = np.matrix(dfStandardizedJMT.T)
ds = dtw.distance_matrix_fast(series)
from dtaidistance import clustering

# Custom Hierarchical clustering
model1 = clustering.Hierarchical(dtw.distance_matrix_fast, {})
# Augment Hierarchical object to keep track of the full tree
model2 = clustering.HierarchicalTree(model1)
# SciPy linkage clustering
model3 = clustering.LinkageTree(dtw.distance_matrix_fast, {})
cluster_idx = model3.fit(series)
model3.plot(ts_height=1000, show_ts_label=True, show_tr_label=True)

sLeft = np.array(dfStandardizedJMT.iloc[:, 2])
sRight = np.array(dfStandardizedJMT.iloc[:, 0])
d, paths = dtw.warping_paths(sLeft, sRight)

print(d)

best_path = dtw.best_path(paths)
print(best_path)
dtwvis.plot_warpingpaths(sLeft, sRight, paths, best_path)
