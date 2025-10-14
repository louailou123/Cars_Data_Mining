import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from CleaningData import CleanData
from VisualizationData import Visualization

df = pd.read_csv("CarPrice_Assignment.csv")
#cleaning data
cleaner=CleanData(df)
print(cleaner.columnsNumber())
print(cleaner.linesNumber())
print(cleaner.variablesInfo())
print(cleaner.showMissingVariables())
cleaner.splitCarNames()
cleaner.ReplaceWrongCarNames()
cleaner.showCleanedCarNames()
#visualization of data
visualater=Visualization(df,plt,sns)
visualater.visualizateX(df["price"],"price",5,5)
visualater.visualizatehistX(df["price"],"price",5,5,5)





