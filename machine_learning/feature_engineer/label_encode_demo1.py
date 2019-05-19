import pandas as pd

from common.pickle_helper import *


class UserLabel(object):

    @staticmethod
    def build_model(df):
        model_dict = {}
        if df.empty:
            return "df is empty"
        feature_list = df.columns.values
        for feature in feature_list:
            values = df[feature].unique()
            value_map = dict(zip(values, [str(i) for i in range(len(values))]))
            # 设置大小写不敏感
            model_dict[feature.lower()] = value_map
        return model_dict

    @staticmethod
    def label_encode(newDataFrame, model):
        feature_list = newDataFrame.columns.values
        for feature in feature_list:
            newDataFrame[feature] = newDataFrame[feature].map(model[feature.lower()])
        return newDataFrame


if __name__ == '__main__':
    df = pd.DataFrame(data=[{'os': 'WINDOWS', 'browser': 'CHROME', 'usertype': 'RETURN', 'ishost': 'TRUE'},
                            {'os': 'MAC', 'browser': 'IE', 'usertype': 'UPDATE', 'ishost': 'FALSE'},
                            {'os': 'TP', 'browser': 'IE', 'usertype': 'UPDATE', 'ishost': 'FALSE'},
                            {'os': 'TP', 'browser': 'FIREFOX', 'usertype': 'UPDATE', 'ishost': 'FALSE'}
                            ])

    user = UserLabel()
    model = user.build_model(df)
    print(model)
    store_model(model, "./model/userLabel.m")

    model = read_model("./model/userLabel.m")
    print(user.label_encode(df, model))
