# coding:utf-8
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
# sns.set()

# %matplotlib inline

#Iris Plot
iris = load_iris()
n_samples, m_features = iris.data.shape

#Load Data
X, y = iris.data, iris.target
D_target_dummy = dict(zip(np.arange(iris.target_names.shape[0]), iris.target_names))

DF_data = pd.DataFrame(X,columns=iris.feature_names)
DF_data["target"] = pd.Series(y).map(D_target_dummy)
#sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  \
#0                  5.1               3.5                1.4               0.2
#1                  4.9               3.0                1.4               0.2
#2                  4.7               3.2                1.3               0.2
#3                  4.6               3.1                1.5               0.2
#4                  5.0               3.6                1.4               0.2
#5                  5.4               3.9                1.7               0.4

DF_dummies = pd.get_dummies(DF_data["target"])
#setosa  versicolor  virginica
#0         1           0          0
#1         1           0          0
#2         1           0          0
#3         1           0          0
#4         1           0          0
#5         1           0          0

from sklearn.preprocessing import OneHotEncoder, LabelEncoder
def f1(DF_data):
    Enc_ohe, Enc_label = OneHotEncoder(), LabelEncoder()
    DF_data["Dummies"] = Enc_label.fit_transform(DF_data["target"])
    DF_dummies2 = pd.DataFrame(Enc_ohe.fit_transform(DF_data[["Dummies"]]).todense(), columns = Enc_label.classes_)
    return(DF_dummies2)

# print pd.get_dummies(DF_data["target"])
#1000 loops, best of 3: 777 µs per loop

print f1(DF_data)
#100 loops, best of 3: 2.91 ms per loop