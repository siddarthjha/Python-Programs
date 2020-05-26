import pandas as p
import numpy as n
"""
out=p.read_csv('sheet.csv')
print(out.head())
print(out.loc[2,'SAP ID'])
z=out.loc[0:5,'SAP ID']
print(z)
"""
l = {'Name':['Siddarth', 'Nikhil', 'Rahul', 'Ayushi', 'Tridib', 'Shristi', 'Siddhanth', 'Aashray', 'Aparna', 'Nitya'],
'Age':[20,19,22,21,20,22,18,20,19,18],'Sex':['M','M','M','F','M','F','M','M','F','F'],'Good':['N','Y','Y','N','N','N','Y','N','Y','Y']
,'x':[n.nan,n.nan,n.nan,n.nan,n.nan,n.nan,n.nan,n.nan,n.nan,n.nan]}

df= p.DataFrame(l)
df.fillna(0)
print(df)
print(df[['Age']])
print(type(df[['Age']]))
print(df.iloc[0:2,0:1])
