#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-29 14:08
# @Author  : erwin


from catboost import CatBoostClassifier

# Initialize data
cat_features = [0, 1]
train_data = [["a", "b", 1, 4, 5, 6], ["a", "b", 4, 5, 6, 7], ["c", "d", 30, 40, 50, 60]]
train_labels = [1, 1, -1]

test_data = [["a", "b", 2, 4, 6, 8], ["a", "d", 1, 4, 50, 60]]
# Initialize CatBoostClassifier
model = CatBoostClassifier(iterations=2, learning_rate=1, depth=2, loss_function='Logloss')
# Fit model
model.fit(train_data, train_labels, cat_features)
# Get predicted classes
preds_class = model.predict(test_data)

# Get predicted probabilities for each class
preds_proba = model.predict_proba(test_data)
print(preds_proba)

# Get predicted RawFormulaVal
preds_raw = model.predict(test_data, prediction_type='RawFormulaVal')
print(preds_raw)