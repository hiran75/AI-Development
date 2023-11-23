import pandas as pd
import tensorflow as tf
# RandomForest활용하여 모델 만들기
from sklearn import svm, metrics
from sklearn.ensemble import RandomForestClassifier
import random, re
import numpy 
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from keras.callbacks import ModelCheckpoint, EarlyStopping
import os
import datetime as dt
import pymssql  
import pandas as pd


filename="cdms0619.csv"

table_name="sjcuclass.dbo.cdms0619"

print(filename)
df=pd.read_csv(filename)
df.rename(columns=lambda x: x.replace(' ', ''), inplace=True)
print(df.describe())
print(df.info())
print(df)


conn = pymssql.connect(server='192.168.100.101', user='sa', password='sjcumscs2204!', database='sjcuclass') 
cursor = conn.cursor()


# Create the table
create_table_query = f'CREATE TABLE {table_name} ('

# Iterate over DataFrame columns to dynamically create table columns
columns_str=""
i=1
for column in df.columns:
    column_name = column.replace(' ', '')  # Replace spaces with underscores
    if i==1:
        columns_str = columns_str +  column_name 
    else:
        columns_str = columns_str + ','+ column_name 

    column_type = 'VARCHAR(500)'  # Set default column type as VARCHAR(255)
    create_table_query += f'{column_name} {column_type}, '
    i=i+1

create_table_query = create_table_query[:-2]  # Remove the trailing comma and space
create_table_query += ')'

# Execute the create table query
#print(create_table_query)
#cursor.execute(create_table_query)
#conn.commit()

#insert_query = f'INSERT INTO {table_name}({columns_str}) VALUES('
inser_query_org = f'INSERT INTO {table_name}({columns_str}) VALUES('  
for row in df.itertuples(index=False):
    #insert_query = f'INSERT INTO {table_name} ({columns_str}) VALUES ({",".join(item for _ in range(len(row)))})'
    #insert_query = f'INSERT INTO {table_name} ({columns_str}) VALUES('
    #values=list(row)
    row_as_list = list(row)
    
    row_as_str = "'"+ "','".join(map(str, row_as_list)) + "')"
    insert_query =inser_query_org+ row_as_str
    print(insert_query)

    #insert_query= insert_query + values
    #print(values)
    cursor.execute(insert_query)
    conn.commit()





# #Close the cursor and connection
cursor.close()
conn.close()
