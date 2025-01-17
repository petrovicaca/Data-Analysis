# -*- coding: utf-8 -*-
"""Vežba_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SzGYcmBfxqheY2Om2ANJZGVUBDnoXfZY
"""

# Commented out IPython magic to ensure Python compatibility.
# import basic libraries
import numpy as np 
import pandas as pd 
import warnings
import os
#warnings.filterwarnings("ignore")

# import plot libraries
import seaborn as sns
sns.set_palette('Set2')
import matplotlib.pyplot as plt
# %matplotlib inline

# import ml libraries
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import linear_model, datasets
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC, SVC
from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()

# import data

from sklearn import linear_model, datasets

train = pd.read_csv("https://raw.githubusercontent.com/hajdeger/AOP_PUB/master/Prvi%20kolokvijum.csv")
test = pd.read_csv("https://raw.githubusercontent.com/hajdeger/AOP_PUB/master/Prvi%20kolokvijum.csv")

# check shape
print("Train rows and columns : ", train.shape)
print("Test rows and columns : ", test.shape)

# check column types
ctype = train.dtypes.reset_index()
ctype.columns = ["Count", "Column Type"]
ctype.groupby("Column Type").aggregate("count").reset_index()
train.info()

# display data header
train.head()

# Let
numeric = ['MPG', 'Cylinders', 'Displacement', "HP",	"Weight", "Acceleration",	"Model year", "Origin"]
train[numeric] = train[numeric].apply(pd.to_numeric, errors='coerce')

train.dtypes

# numerical data distribution
train.describe()

# categorical data distribution
train.describe(include=["O"])

# check missing values
missing_df = train.isnull().sum(axis=0).reset_index()
missing_df.columns = ["column_name", "missing_count"]
missing_df = missing_df[missing_df["missing_count"]>0]
missing_df = missing_df.sort_values(by="missing_count")
missing_df

# impute/treat missing values
train["Car name"] = train["Car name"].fillna(train["Car name"].value_counts().index[0]) 
train["MPG"].fillna(train["MPG"].mean(), inplace=True) # for numerical (mean or median)
train["HP"].fillna(train["HP"].mean(), inplace=True) # for numerical (mean or median)
train["Acceleration"].fillna(train["Acceleration"].mean(), inplace=True) # for numerical (mean or median)
train["Weight"].fillna(train["Weight"].mean(), inplace=True) # for numerical (mean or median)
train["Displacement"].fillna(train["Displacement"].mean(), inplace=True) # for numerical (mean or median)
train["Cylinders"].fillna(train["Cylinders"].mean(), inplace=True) # for numerical (mean or median)
#train["Model year	"].fillna(train["Model year	"].mean(), inplace=True) # for numerical (mean or median)



# check missing values
missing_df = train.isnull().sum(axis=0).reset_index()
missing_df.columns = ["column_name", "missing_count"]
missing_df = missing_df[missing_df["missing_count"]>0]
missing_df = missing_df.sort_values(by="missing_count")
missing_df

# histogram of numerical column
plt.figure(figsize=(12,8))
sns.distplot(train["Weight"].values, bins=10, kde=False)
plt.xlabel("Weight", fontsize=12)
plt.title("Weight histogram", fontsize=14)
plt.show()

sns.regplot(x="MPG", y="Weight", data=train) # numerical vs numerical

# multivariate analysis
temp = train[numeric]
corrmat = temp.corr(method="spearman")
f, ax = plt.subplots(figsize=(20, 20))
sns.heatmap(corrmat, vmax=1., square=True, cmap="YlGnBu", annot=True)
plt.title("numerical variables correlation map", fontsize=15)
plt.show()