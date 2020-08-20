import pandas as pd
import os

#Initialize csv file path
CSV_FILE=os.path.join('C:/Users/lic/.spyder-py3','artwork_data.csv')

#Read entire dataframe
df=pd.read_csv(CSV_FILE,
                    index_col='id')

#Creating group of dataframe for each artist
grouped=df.groupby('artist')
type(grouped)

#Displaying minimum acquisition year for each artist
for name, df_group in grouped:
    MIN_ACQ_YEAR=df_group['acquisitionYear'].min()
    print('{0} --> {1}'.format(name,MIN_ACQ_YEAR))

