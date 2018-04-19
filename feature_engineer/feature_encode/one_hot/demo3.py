# from sklearn import preprocessing
#
# enc = preprocessing.OneHotEncoder()
# enc.fit([['a', 'b'], ['c', 'd']])


import pandas as pd
from feature_engineer.category_encode import user_label

df = pd.DataFrame(data=[{'os': 'WINDOWS', 'browser': 'CHROME', 'usertype': 'RETURN', 'ishost': 'TRUE'},
                        {'os': 'MAC', 'browser': 'IE', 'usertype': 'UPDATE', 'ishost': 'FALSE'},
                        {'os': 'TP', 'browser': 'IE', 'usertype': 'UPDATE', 'ishost': 'FALSE'},
                        {'os': 'TP', 'browser': 'FIREFOX', 'usertype': 'UPDATE', 'ishost': 'FALSE'}
                        ])




