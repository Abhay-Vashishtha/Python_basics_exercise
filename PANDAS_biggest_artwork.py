# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:38:13 2020

@author: lic
"""


import pandas as pd
import os

#Initialize csv file path
CSV_FILE=os.path.join('C:/Users/lic/.spyder-py3','artwork_data.csv')

#Read entire dataframe
df=pd.read_csv(CSV_FILE,
                    index_col='id',)

#force convert width and column values to numeric type to avoid errors
df['width']=pd.to_numeric(df['width'],errors='coerce')
df['height']=pd.to_numeric(df['height'],errors='coerce')

#Calculating area and adding field AREA to dataframe
area=df['height']*df['width']
df=df.assign(AREA=area)

#displaying the biggest artwork
df_biggest_artwork=df.loc[df['AREA'].idxmax(),:]