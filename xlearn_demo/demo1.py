#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/17 10:13 AM
# @Author : Erwin
import xlearn as xl

# Training task
ffm_model = xl.create_ffm()                # Use field-aware factorization machine (ffm)
ffm_model.setTrain("./small_train.txt")    # Set the path of training dataset
ffm_model.setValidate("./small_test.txt")  # Set the path of validation dataset
param = {'task':'binary', 'lr':0.2, 'lambda':0.002, 'metric':'acc'}
ffm_model.fit(param, './model.out')

# Prediction task
ffm_model.setTest("./small_test.txt")  # Set the path of test dataset
ffm_model.setSigmoid()                 # Convert output to 0-1

# Start to predict
# The output result will be stored in output.txt
ffm_model.predict("./model.out", "./output.txt")