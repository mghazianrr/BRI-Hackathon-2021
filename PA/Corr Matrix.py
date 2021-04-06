# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:15:30 2020

@author: Ghazian
"""

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
dff =  df.drop(['job_level', 'person_level', 'Employee_type', 'Employee_status', 'gender', 'marital_status_maried(Y/N)', 'Education_level', 'year_graduated', 'achievement_target_1', 'achievement_target_2', 'achievement_target_3'], axis = 1)
corrMatrix = dff.corr()
#print(corrMatrix)

sn.heatmap(corrMatrix, annot = True)
plt.figure(figsize=(10, 10))
plt.show