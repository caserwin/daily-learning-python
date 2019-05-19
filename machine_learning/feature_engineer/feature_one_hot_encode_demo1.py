from sklearn import preprocessing
from common.pickle_helper import *

data = [[0, 0, 3],
        [1, 1, 0],
        [0, 2, 1],
        [1, 0, 2]]

enc = preprocessing.OneHotEncoder()
enc.fit(data)
print("每个维度值得个数：" + str(enc.n_values_))
store_model(enc, "./model/feature.m")

enc = read_model("./model/feature.m")
print(enc.transform([[0, 1, 3]]).toarray())
print(enc.transform([[0, 1, 1]]).toarray())
