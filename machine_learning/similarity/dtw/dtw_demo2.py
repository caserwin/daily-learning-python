#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-14 15:35
# @Author  : erwin
from dtaidistance import dtw
import pandas as pd
import numpy as np
from dtaidistance import clustering
from common.util_function import *
from machine_learning.similarity.dtw.hierarchical_helper import ClusterHelper
from machine_learning.similarity.dtw.hierarchical_helper import HierarchicalHelper

print_line("distance_matrix_fast 测试")
s1 = [0, 0, 1, 2, 1, 0, 1, 0]
s2 = [0, 1, 2, 0, 0, 0, 0, 0]
s3 = [0, 0, 1, 2, 1, 0, 0, 0]

distance12, paths12 = dtw.warping_paths(s1, s2)
distance13, paths13 = dtw.warping_paths(s1, s3)
distance23, paths23 = dtw.warping_paths(s2, s3)

print("distance12:", distance12, " distance13:", distance13, " distance23:", distance23, "\n")

data = np.array([[0, 0, 0, 1, 3],
                 [0, 1, 0, 2, 4],
                 [1, 2, 1, 1, 5],
                 [2, 0, 2, 2, 1],
                 [1, 0, 1, 1, 0],
                 [0, 0, 0, 2, 0],
                 [1, 0, 0, 1, 1],
                 [0, 0, 0, 2, None]])

df = pd.DataFrame(data=data).fillna(0)
series = np.matrix(df.T, dtype=np.double)
ds = dtw.distance_matrix_fast(series)
print_br(ds)

print_line("Hierarchical clustering")
model3 = clustering.LinkageTree(dtw.distance_matrix_fast, {})
model3.fit(series)
model3.plot(show_ts_label=True, show_tr_label=True)
model3.plot(filename="./clustered.png", show_ts_label=True, show_tr_label=True)
print(model3.to_dot())

# 构建树的数据结构
tree_helper = HierarchicalHelper(model3)
print(tree_helper.root, tree_helper.root.isLeaf())
print(tree_helper.root.left_node, tree_helper.root.left_node.isLeaf())
print(tree_helper.root.right_node, tree_helper.root.right_node.isLeaf())

# 建立子节点到父节点的映射
cls_helper = ClusterHelper(model3, len(series))
print(cls_helper.toMap())

# 根据指定类别数，返回所有类别
cluster_keys = tree_helper.getClusterByNum(tree_helper.root, 3, {})
for i in cluster_keys:
    print(i)

# 根据指定最小距离，返回所有类别
cluster_keys = tree_helper.getClusterByDist(tree_helper.root, 6, {})
for i in cluster_keys:
    print(i)

# 返回一个节点下所有子节点
nodes = []
tree_helper.iterTree(tree_helper.root.right_node, nodes)
for node in nodes:
    print(node)

# 根据idx 返回节点实例
print("=" * 10)
print(tree_helper.idx_node_map.get(0))
