import pandas as pd
import pickle


class UserOneHot(object):

    def buildModel(self, dataFrame):
        model_dict = {}
        if dataFrame.empty:
            return "df is empty"
        feature_list = dataFrame.columns.values
        for feature in feature_list:
            values = dataFrame[feature].unique()
            value_map = dict(zip(values, range(len(values))))
            # 设置大小写不敏感
            model_dict[feature.lower()] = value_map
        return model_dict

    def oneHotEncode(self, newDataFrame, model):
        feature_list = newDataFrame.columns.values
        for feature in feature_list:
            newDataFrame[feature] = newDataFrame[feature].map(model[feature.lower()])
        return newDataFrame

    def storeTree(self, filename, model_dict):
        if model_dict == {}:
            return "model is empty"
        fw = open(filename, 'wb')
        # 对象持久化包
        pickle.dump(model_dict, fw)
        fw.close()

    def grabTree(self, filename):
        fr = open(filename, 'rb')
        return pickle.load(fr)


if __name__ == '__main__':
    user = UserOneHot()
    df = pd.DataFrame(data=[{'os': 'WINDOWS', 'browser': 'CHROME', 'usertype': 'RETURN', 'ishost': 'TRUE'},
                            {'os': 'MAC', 'browser': 'IE', 'usertype': 'UPDATE', 'ishost': 'FALSE'},
                            {'os': 'TP', 'browser': 'IE', 'usertype': 'UPDATE', 'ishost': 'FALSE'},
                            {'os': 'TP', 'browser': 'FIREFOX', 'usertype': 'UPDATE', 'ishost': 'FALSE'}
                            ])
    model = user.buildModel(df)
    print(model)

    print(df)
    print(user.oneHotEncode(df, model))
