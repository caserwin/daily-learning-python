# coding:utf-8
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.externals import joblib


def cate_coding(DF_data):
    Enc_ohe, Enc_label = OneHotEncoder(), LabelEncoder()
    DF_data["Dummies"] = Enc_label.fit_transform(DF_data["target"])
    DF_dummies2 = pd.DataFrame(Enc_ohe.fit_transform(DF_data[["Dummies"]]).todense(), columns=Enc_label.classes_)
    return (DF_dummies2)


if __name__ == '__main__':
    iris = load_iris()
    n_samples, m_features = iris.data.shape
    X, y = iris.data, iris.target

    # 类别编码, 1,2,3
    D_target_dummy = dict(zip(np.arange(iris.target_names.shape[0]), iris.target_names))
    # {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

    # 构建 dataframe，把 0，1，2 映射为类别名
    DF_data = pd.DataFrame(X, columns=iris.feature_names)
    DF_data["target"] = pd.Series(y).map(D_target_dummy)
    # print(DF_data)

    # 方式一：通过get_dummies对类别进行 one - hot 编码
    DF_dummies = pd.get_dummies(DF_data["target"])
    print(DF_dummies)

    # 方式二：通过 OneHotEncoder, LabelEncoder 对类别进行 one - hot 编码
    print(cate_coding(DF_data))

    # 方式三：加载模型的方式
    # joblib.dump(le, "label1.m")
    le = joblib.load("./model/label1.m")
    print(le.transform(["a2", "a2", "a3"]))
