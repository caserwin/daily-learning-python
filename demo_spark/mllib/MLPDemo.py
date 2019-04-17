# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 下午7:24
# @Author  : yidxue

# MLP 是一种前向结构的人工神经网络。一个MLP至少由三层节点组成。除输入节点外，每个节点都是使用非线性激活函数的神经元。
# MLP使用称为“反向传播”的监督学习技术进行训练。其多层和非线性激活将MLP与线性感知器区分开来。
# 它可以区分不能线性分离的数据。
# https://www.toutiao.com/a6552804995442409991/?tt_from=weixin&utm_campaign=client_share&timestamp=1525776941&app=news_article&utm_source=weixin&iid=31973047962&utm_medium=toutiao_android&wxshare_count=1

import pyspark.sql.functions as F
from pyspark.ml import Pipeline
from pyspark.ml import PipelineModel
from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import VectorAssembler, StringIndexer, VectorIndexer, IndexToString
from pyspark.sql import SparkSession
from pyspark.sql.types import *


def string_to_float(x): return float(x)


spark = SparkSession.builder.appName('RN').getOrCreate()
string_to_float_udf = F.udf(string_to_float, DoubleType())
animal_udf = F.udf(lambda x: condition(x), StringType())


def condition(r):
    if r == 1:
        label = "Mamal"
    elif r == 2:
        label = "Bird"
    elif r == 3:
        label = "Reptile"
    elif r == 4:
        label = "Fish"
    elif r == 5:
        label = "Amphibian"
    elif r == 6:
        label = "Bug"
    else:
        label = "Invertebrate"
    return label


def get_df_columns_train(df):
    df_train = df \
        .select(F.col("animal_name").cast("String"),
                F.col("hair").cast("Double"),
                F.col("feathers").cast("Double"),
                F.col("eggs").cast("Double"),
                F.col("milk").cast("Double"),
                F.col("airborne").cast("Double"),
                F.col("aquatic").cast("Double"),
                F.col("predator").cast("Double"),
                F.col("toothed").cast("Double"),
                F.col("backbone").cast("Double"),
                F.col("breathes").cast("Double"),
                F.col("venomous").cast("Double"),
                F.col("fins").cast("Double"),
                F.col("legs").cast("Double"),
                F.col("tail").cast("Double"),
                F.col("domestic").cast("Double"),
                F.col("catsize").cast("Double"),
                F.col("class_type").cast("Double").alias("label")) \
        .withColumn("label", animal_udf(F.col("label")))

    return df_train


def get_df_columns_test(df):
    df_test = df.select(F.col("animal_name").cast("String"),
                        F.col("hair").cast("Double"),
                        F.col("feathers").cast("Double"),
                        F.col("eggs").cast("Double"),
                        F.col("milk").cast("Double"),
                        F.col("airborne").cast("double"),
                        F.col("aquatic").cast("double"),
                        F.col("predator").cast("double"),
                        F.col("toothed").cast("double"),
                        F.col("backbone").cast("double"),
                        F.col("breathes").cast("double"),
                        F.col("venomous").cast("double"),
                        F.col("fins").cast("double"),
                        F.col("legs").cast("double"),
                        F.col("tail").cast("double"),
                        F.col("domestic").cast("double"),
                        F.col("catsize").cast("double"))
    return df_test


def df_train():
    df = spark.read.format("com.databricks.spark.csv").option("header", "true").load("data/zoo.csv")
    df = get_df_columns_train(df)
    assembler = VectorAssembler(inputCols=df.columns[1:-1], outputCol='features')
    features = assembler.transform(df)
    labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(features)
    featureIndexer = VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=3).fit(features)
    (trainingData, testData) = features.randomSplit([0.8, 0.2])
    layers = [16, 5, 4, 4, 7]
    trainer = MultilayerPerceptronClassifier(labelCol="indexedLabel", featuresCol="indexedFeatures", maxIter=100,
                                             layers=layers, blockSize=128, seed=1234)
    labelConverter = IndexToString(inputCol="prediction", outputCol="predictedLabel", labels=labelIndexer.labels)
    pipeline = Pipeline(stages=[labelIndexer, featureIndexer, trainer, labelConverter])
    model = pipeline.fit(trainingData)
    predictions = model.transform(testData)
    model.write().overwrite().save("data/RN")
    predictions.select("prediction", "indexedLabel", "features").show(5)
    evaluator = MulticlassClassificationEvaluator(labelCol="indexedLabel", predictionCol="prediction",
                                                  metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Predictions accuracy = %g, Test Error = %g" % (accuracy, 1 - accuracy))
    return model


def df_test():
    df = spark.read.format("com.databricks.spark.csv").option("header", "true").load("data/zoo.csv")
    df = get_df_columns_test(df)
    assembler = VectorAssembler(inputCols=df.columns[1:], outputCol='features')
    pipeline = Pipeline(stages=[assembler])
    pipelineModel = pipeline.fit(df)
    dataset = pipelineModel.transform(df)
    loadedPipeline = PipelineModel.read().load("data/RN")
    predictions = loadedPipeline.transform(dataset)
    return predictions


if __name__ == '__main__':
    my_model = df_train()
    df2 = df_test()
    df2_select = df2.select("animal_name", "predictedLabel")
    print(df2_select.toPandas())
