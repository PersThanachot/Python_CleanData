from numpy import dtype #type of data frame
import pandas as pd     #Library for DataFrame
import math 

#input data from file csv
df = pd.read_csv("___Location_File___")
print(df.head)
print(df.info())

#check type of data
print(df.dtypes)

#rename column
df = df.rename(columns={'ARM_ACC_NO'        :'Column_1',
                        'ARM_PAYMENT_TYPE'  :'Column_2',
                        'ARM_FINANCE_AMT'   :'Column_3',
                        'ARM_CASH_PRICE'    :'Column_4',
                        'ARM_HP_PRICE'      :'Column_5',})

#Select Column
df1 = df[['Column_1','Column_2','Column_3']]
print(df1)
print(df1.dtypes)

#data test for rbine
df2 = pd.DataFrame({'Column_1':[123456,999888],'Column_2':['OK',''],'Column_3':[1.5,1.2]})
print(df2)
print(df2.dtypes)

# row bine
df3 = pd.concat([df1,df2])
print(df3)

#save_csv
df3.to_csv("___Location_File___")

#rename variable in Column
df3.loc[df3['Column_2'] == 'DPS', 'Column_4'] = 'OK!!!'
df3.loc[df3['Column_2'] == 'DPS', 'Column_2'] = 'OK!!!'
print(df3)

#drop column
df3 = df3.drop('Column_4',axis = 1) # axis = 1 is column | axis = 0 is row

#filter
df4 = df3[(df3["Column_2"] == 'OK') | (df3["Column_2"] == '')]
df4 == ''
print(df4)

#is real NA
df4.loc[df4['Column_2'] == '', 'Column_2'] = float('NaN')
print(df4)

#check NA
pd.isna(df4)
df4.isnull().sum() #very good

print(df4.info())

#remove NA
df4.dropna(axis = 0 ,how = 'any' ,inplace=True) #float('NaN') is real NA of Python
print(df4)

# Chnage Type data
df1['Column_3'] = pd.to_numeric(df1['Column_3'],downcast='integer') #ลดขนาดข้อมูล interger หรือ float
print(df1.dtypes)

df1[['Column_3']] = df[['Column_3']].astype('int') # int(ตัวเลข)|category(ประเภท)|float(ทศนิยม)|str(object)|bool(true/false)|timedelta(Differences between two datetimes)
print(df1.dtypes)

#create date
date1 = pd.Series(pd.date_range('20210731', periods=3)) # date 3 day
print(date1)

date555 = {'Month' : [1,2,3],
           'Day' : [31,1,2],
           'Year': [2021,2021,2021]}
date555 = pd.DataFrame(date555)
print(date555)

date2 = pd.to_datetime(date555[['Month', 'Day', 'Year']])
print(date2)

