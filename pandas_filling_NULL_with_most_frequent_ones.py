# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:47:33 2020

@author: lic
"""


import pandas as pd
import os

#Initialize csv file path
CSV_FILE=os.path.join('C:/Users/lic/.spyder-py3','artwork_data.csv')

#Read entire dataframe
df=pd.read_csv(CSV_FILE,
                    index_col='id')

#Filling in empty fields with most frequent ones

#Defining empty list
group_list=[]

#Filling empty field with most frequent one in the group and appending to list
for name, group in df.groupby('artist'):
    group=group.fillna(group['artistId'].value_counts().index[0])
    group_list.append(group)

#Concatenating the list elements into output DataFrame
df_out=pd.concat(group_list)
