#Given a csv file for class data
#Seperate the data on basis of class
#Output the separated data in an excel workbook in different sheets

import pandas as pd
import os

#Fetching file name
csv_file=os.path.join('C:/Users/lic/.spyder-py3','class_data.csv')

#Creating source dataframe
df=pd.read_csv(csv_file)

#Creating wrter for excel workbook
writer=pd.ExcelWriter('out_class.xlsx',engine='xlsxwriter')

#Create sheet in workbook for source dataset
df.to_excel(writer,sheet_name="All Classes",index=False)

#Separating datasets on basis of class and putting in different sheets
for name,group in df.groupby('Class'):
    group.to_excel(writer,sheet_name='Class {}'.format(name),index=False)

#Saving excel sheet
writer.save()