# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 00:37:43 2017

@author: Sujay N
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Starbucks_store_locations.csv")
df1 = (df.notnull().sum()*100)/df.shape[0]
print("completeness percentage")
print(df1)

print("Number of Countries Where Starbucks Operates")
print(len(df['Country'].unique()))

print("Countries With Maximum Number of Stores all over World")
df2 = df["Country"].value_counts().head(10)
print((df2))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
df2.plot(kind =' bar',color = "red")

print("Cities With Maximum Number of Stores all over World")
df3 = df["City"].value_counts().head(10)
print((df3))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
df3.plot(kind =' bar',color = "green")

print("Ownership Type of Stores")
df4 = df["Ownership Type"].value_counts()
print(df4)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
df4.plot(kind =' bar',color = "blue")

print("States of USA with Maximum Number of stores")
df5= df[df["Country"]== 'US']
df6 = df5["State/Province"].value_counts().head(10)
print(df6)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
df6.plot(kind =' bar',color = "orange")

