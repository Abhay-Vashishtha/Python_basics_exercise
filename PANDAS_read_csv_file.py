# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 20:08:53 2020


"""


import pandas as pd
import os

#Initialize csv file path
CSV_FILE=os.path.join('path','artwork_data.csv')

#Read sample data to see how file looks
df_sample=pd.read_csv(CSV_FILE,nrows=5)

#Specify an index
df_sample_index=pd.read_csv(CSV_FILE,nrows=5,index_col='id')

#limit Column
df_sample_column=pd.read_csv(CSV_FILE,nrows=5,index_col='id',usecols=['id','artist','url'])

#Proper data loading

COLS_TO_USE=['id','artist','title','medium','year','acquisitionYear','width','height','units']

df=pd.read_csv(CSV_FILE,
               usecols=COLS_TO_USE,
               index_col='id')
