import pandas as pd
import pickle


class UserLabel(object):

    def buildModel(self, dataFrame):
        model_dict = {}
        if dataFrame.empty:
            return "df is empty"
        feature_list = dataFrame.columns.values
        for feature in feature_list:
            values = dataFrame[feature].unique()
            value_map = dict(zip(values, [str(i) for i in range(len(values))]))
            # 设置大小写不敏感
            model_dict[feature.lower()] = value_map
        return model_dict

    def labelEncode(self, newDataFrame, model):
        feature_list = newDataFrame.columns.values
        for feature in feature_list:
            newDataFrame[feature] = newDataFrame[feature].map(model[feature.lower()])
        return newDataFrame

    def store(self, model_dict, filename):
        if model_dict == {}:
            return "model is empty"
        fw = open(filename, 'wb')
        # 对象持久化包
        pickle.dump(model_dict, fw)
        fw.close()

    def get(self, filename):
        fr = open(filename, 'rb')
        return pickle.load(fr)
