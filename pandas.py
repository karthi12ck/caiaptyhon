# -*- coding: utf-8 -*-
"""
Created on Fri May 31 08:49:38 2019

@author: Training23
"""

#1
def pandas():
    import pandas as pd
    print(pd.__version__)
    print(help(pd))
#2
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
 'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
 'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df=pd.DataFrame(data)

df.describe()
df.iloc[:3]
df[['age','animal']]
df.iloc[1:2,0:1]
print(df['animal'].iloc[3], df['age'].iloc[3])
print(df['animal'].iloc[4],df['age'].iloc[4])
print(df['animal'].iloc[8], df['age'].iloc[8])
print(df[df['visits'] > 3])
print(df[df['age'].isnull()])
print(df[(df['age'] >= 2) & (df['age'] <= 4)])
print(df.sum(axis=0,skipna=True,numeric_only =True))

df.loc['k']=[2.5,'cat','no',1]
df.drop('k')
df['priority'] = df['priority'].map({'yes': True, 'no': False})


#3
 

df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
df.sub(axis=1,df.mean(axis=0))
df.mean(axis=0)

#7Create a pandas series from: a list, numpy and a dictionary

c=np.random.rand(0,100)
data=pd.Series(c)

t=[x**2 for x in range(0,10)]
date2=pd.Series()



