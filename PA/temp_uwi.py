# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import*
import seaborn as sb
import numpy as np


df = pd.read_csv(r'train.csv')

#print(df['Last_achievement_%'].median())

df['achievement_target_1'].replace(np.NaN, str(df['achievement_target_1'].mode())) #filling missing values
a=list(df['achievement_target_1'])
le = preprocessing.LabelEncoder()
le.fit(a)                                  #proses fitting kelas dalam list a
df['achievement_target_1']=le.transform(a) #proses transformasi kolom data berdasarkan fitting line diatas

df['achievement_target_2'].replace(np.NaN, str(df['achievement_target_2'].mode()))
a=list(df['achievement_target_2'])
le.fit(a)
df['achievement_target_2']=le.transform(a)

df['achievement_target_3'].replace(np.NaN, str(df['achievement_target_3'].mode()))
a=list(df['achievement_target_3'])
le.fit(a)
df['achievement_target_3']=le.transform(a)

df['Last_achievement_%'].replace(np.NaN, float(df['Last_achievement_%'].mean()))
df['Achievement_above_100%_during3quartal'].replace(np.NaN, float(df['Achievement_above_100%_during3quartal'].mean()))

#sb.distplot(df['Last_achievement_%'], kde = False)
#plt.show()

df.to_csv('train_mean.csv')