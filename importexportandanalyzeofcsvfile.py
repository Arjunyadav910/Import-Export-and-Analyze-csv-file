import pandas as pd
readfile=pd.read_csv("Details.csv")
# readfile
# readfile.tail()
# readfile.describe()
# readfile.head()
# readfile.sample()
# readfile.info()
# readfile.dtypes
# readfile.shape
# readfile.columns
# readfile["Amount"].sum()
# readfile.loc[56]
# readfile.isnull()
# readfile.notnull()
# storefile=readfile.sample(10)
# storefile
# storefile.to_csv("file.csv")
# print(readfile.isnull().sum())
# print(readfile.dropna().isnull().sum())
# readfile.fillna()
# new=readfile.replace("Furniture","Arjun") // export file to the new variable
# new
# new.to_csv("newdetails1.csv")
# fillvalue=new.fillna("Arjun")
# fillvalue
# fillvalue.to_csv("newdetails2.csv")
# analyzedf=fillvalue.drop_duplicates()
# analyzedf.index
# analyzedf.to_csv("newdetails3.csv")
analyzedf.index
