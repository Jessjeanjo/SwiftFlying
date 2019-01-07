#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 08:13:54 2018

@author: bald
"""

# Import Libraries
import numpy as npy
import matplotlib.pyplot as pplot
import pandas

from sklearn.preprocessing import Imputer

# Import dataset
dataset = pandas.read_csv('Data.csv')
mat_feat = dataset.iloc[:, :-2].values
dep_vec = dataset.iloc[:, -2].values

# Take care of missing data
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(mat_feat[:, 1:3])
mat_feat[:, 1:3] = imputer.transform(mat_feat[:, 1:3])










