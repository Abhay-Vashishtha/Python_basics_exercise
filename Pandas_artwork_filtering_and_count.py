import pandas as pd
import os

#Initialize csv file path
CSV_FILE=os.path.join('C:/Users/lic/.spyder-py3','artwork_data.csv')

#Read entire dataframe
df_full=pd.read_csv(CSV_FILE,
                    index_col='id',)

#Filter id,artist, title and url for artist named 'Blake, William' 

COLS_TO_USE=['id','artist','title','url']
df_sel_cols=pd.read_csv(CSV_FILE,
                        usecols=COLS_TO_USE,
                        index_col='id')

df_filtered=df_sel_cols[df_sel_cols['artist']=='Blake, William']

#Reading count of artist 'Blake, William

artist_counts=df_full['artist'].value_counts()

artist_counts_Blake=artist_counts['Blake, William']
