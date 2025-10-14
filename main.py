from CleaningData import CleanData
import pandas as pd
df = pd.read_csv("CarPrice_Assignment.csv")
cleaner=CleanData(df)
print(cleaner.columnsNumber())
print(cleaner.linesNumber())
print(cleaner.variablesInfo())
print(cleaner.showMissingVariables())
cleaner.splitCarNames()
cleaner.ReplaceWrongCarNames()
cleaner.showCleanedCarNames()




