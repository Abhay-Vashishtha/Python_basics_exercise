import pandas as pd
import os

#Initialize csv file path
CSV_FILE=os.path.join('C:/Users/lic/.spyder-py3','artwork_data.csv')

#Read entire dataframe
df_full=pd.read_csv(CSV_FILE,
                    index_col='id',)

#demonstrating use of loc and iloc
#loc is selecting by label
#iloc is selecting by position

#Selecting by label

df_l1=df_full.loc[1035,'artist']
df_l2=df_full.loc[df_full['artist']=='Blake, Robert', : ]

#Selecting by position

df_p1=df_full.iloc[2:4,[0,1,5]]
