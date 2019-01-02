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

# Import dataset
dataset = pandas.read_csv('Data.csv')
mat_feat = dataset.iloc[:, :-2].values
dep_vec = dataset.iloc[:, -2].values











