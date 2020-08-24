# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:11:56 2020

@author: lic
"""


import pandas as pd
import os

#Initialize csv file path
CSV_FILE=os.path.join('C:/Users/lic/.spyder-py3','class_data.csv')

#Read entire dataframe
df=pd.read_csv(CSV_FILE)

list_class5=[]
list_class6=[]

for name, group in df.groupby('Class'):
    if name==5:
        df_class5=group.iloc[:,[0,2,3]]
    else:
        df_class6=group.iloc[:,[0,2,3]]
