import pandas as pd
import sys
import re
import io 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sys.stdout= io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


df = pd.read_csv("CarPrice_Assignment.csv")
''' calcule de lignes et de colones'''
print(f"nombre de lignes {df.shape[0]}")
print(f"nombre de colones {df.shape[1]}")
''' affiche les types de variables qualitatives et quantitatives'''
print(df.info())
''' affiche le nombre des valuers manquantes '''
print(df.isnull().sum())
''' visualiser la variable cible '''
plt.figure(figsize=(6,4))
sns.boxplot(x=df["price"])
plt.title("Box Plot de la variable cible (price)")
plt.show()

# Tracé de distribution (histogramme + courbe KDE)
plt.figure(figsize=(6,4))
sns.histplot(df["price"])
plt.title("Distribution de la variable cible (price)")
plt.show()

df['CleanedCarName'] = df['CarName'].str.split(' ', expand=True).loc[:, 0]

df['CleanedCarName']= df['CleanedCarName'].replace({
    "maxda":"mazda",
    "vw":"bmw",
    "vokswagen":"volkswagen",
    "porcshce":"porsche",
    "Nissan":"nissan",
    "toyouta":"toyota"
    
    
})
print(df["CleanedCarName"].value_counts())

plt.figure(figsize=(15,15))
sns.histplot(df["CleanedCarName"],shrink=0.4)
plt.title("HISTOGRAM OF CARS BY NAME")
plt.xticks(fontsize=5)
plt.show()