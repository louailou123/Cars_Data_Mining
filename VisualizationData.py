
class Visualization :
    def __init__(self,df,plt,sns):
        self.df=df
        self.plt=plt
        self.sns=sns
    def visualizateX (self,x,name,width,height):
        self.plt.figure(figsize=(width,height))
        self.sns.boxplot(x=x)
        self.plt.title(f"box plot of {name}")
        self.plt.show()
    def visualizatehistX (self,x,name,width,height,fontsize):
        self.plt.figure(figsize=(width,height))
        self.sns.histplot(x=x)
        self.plt.title(f"Distribution of {name}")
        self.plt.xticks(fontsize=fontsize)
        self.plt.show()
