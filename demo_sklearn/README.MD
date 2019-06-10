## 1. 特征重要性

1. 去掉、增加这个特征，查看模型在验证集或测试集上的效果。优点是直接看结果，比较准，缺点是复杂度太高了，每次都要重新训练模型跑预测；
2. 树模型可以输出特征重要度。比如XGboost，RandomForest等，可以在训练完成后输出特征的重要程度，排序依据有两种：1根特特征被作为最佳划分特征的次数；2使用该特征划分后的得到信息增益大小；
3. 使用Logistic Regression线性模型，可以直接查看其权重得到重要程度；
4. 可以利用皮尔逊相关系数等，查看特征和类别的关系，也能在一定程度上判别特征重要程度

## 2. 特征选择
选择好的特征可以通过减少参数来避免过拟合，并且减少计算时间，提高精度（特别是在高维数据上），步骤：

1. 用参数搜索器：GridSearchCV搜索一个模型最优参数。
2. 根据这个最优参数训练模型，如（LR）。
3. 根据第2步的模型来选择最优几个特征。
4. 拿到最优的少数几个特征后，重新训练模型。(SelectKBest, SelectFromModel交叉验证，选择模型，避免过拟合)

[sklearn_basic_feature_select_LR_Lasso2.py](https://github.com/caserwin/daily-learning-python/blob/master/demo_sklearn/sklearn_basic_feature_select_LR_Lasso2.py)


## 3. 类别不平衡数据
 
1. Undersampling the majority class
2. Oversampling the minority class
3. Using K-means clustering to undersample
4. Using SMOTE(Synthetic Minority Over-Sampling Technique) to oversample

[Credit Card Fraud Detection](https://www.kaggle.com/dkim1992/classifying-unbalanced-data-fraud-detection)

## 4. 数据集
1. [Feature Selection/Ranking Methods](https://www.kaggle.com/dkim1992/feature-selection-ranking/data)

## 5. 调参经验
1. [scikit-learn 梯度提升树(GBDT)调参小结](https://www.cnblogs.com/pinard/p/6143927.html)