from sklearn import preprocessing
enc = preprocessing.OneHotEncoder()
enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
print(enc.n_values_)
from sklearn.externals import joblib
joblib.dump(enc, "feature.m")

enc = joblib.load("feature.m")
print(enc.transform([[0, 1, 3]]).toarray())
print(enc.transform([[0, 1, 1]]).toarray())
