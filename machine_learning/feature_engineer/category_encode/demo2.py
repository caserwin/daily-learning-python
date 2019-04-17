
import pandas as pd
from machine_learning.feature_engineer.category_encode import UserLabel

if __name__ == '__main__':

    df = pd.DataFrame(data=[{'os': 'WINDOWS', 'browser': 'CHROME', 'usertype': 'RETURN', 'ishost': 'TRUE'},
                        {'os': 'MAC', 'browser': 'IE', 'usertype': 'UPDATE', 'ishost': 'FALSE'},
                        {'os': 'TP', 'browser': 'IE', 'usertype': 'UPDATE', 'ishost': 'FALSE'},
                        {'os': 'TP', 'browser': 'FIREFOX', 'usertype': 'UPDATE', 'ishost': 'FALSE'}
                        ])

    user = UserLabel()
    # model = user.buildModel(df)
    # print(model)
    # user.store(model, "userLabel.m")

    model = user.get("userLabel.m")
    print(user.labelEncode(df, model))