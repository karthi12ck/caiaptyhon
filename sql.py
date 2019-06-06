# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:53:37 2019

@author: Training23
"""

import pandas as pd
import sqlalchemy
import urllib
quoted = urllib.parse.quote_plus('Driver={SQL Server Native Client 11.0};'
                'Server=ssintr02;'
                'Database=T5_Karthick;'
                'uid=T5_Karthick;'
                'pwd=Karthi@12;')
engine=sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

sql='select * from northwind.dbo.orders'
df=pd.read_sql(sql,engine)

df.to_sql('test2',con=engine,if_exists='replace',index=False) #/replace

