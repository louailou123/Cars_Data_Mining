
class CleanData:
    def __init__(self,df):
        self.df=df
    def getDataFrame(self):
        return (self.df)
    def columnsNumber (self):
        return (self.df.shape[0])
    def linesNumber (self):
        return (self.df.shape[1])
    def variablesInfo (self):
        return (self.df.info())
    def showMissingVariables (self) :
        return (self.df.isnull().sum())
    def splitCarNames (self):
        self.df['CleanedCarName']=self.df['CarName'].str.split(' ', expand=True).loc[:, 0]
    def ReplaceWrongCarNames (self):
        self.df['CleanedCarName']=self.df['CleanedCarName'].replace({
    "maxda":"mazda",
    "vw":"bmw",
    "vokswagen":"volkswagen",
    "porcshce":"porsche",
    "Nissan":"nissan",
    "toyouta":"toyota"
    
    
})
    def showCleanedCarNames (self):
        print (self.df['CleanedCarName'].value_counts())