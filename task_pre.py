# data preprocessing
import pandas as pd
import numpy as np

df = pd.read_excel("report(2).xlsx", keep_default_na=False, header=None)
# pre processing
#removing rows from head or tail
df.drop(df.head(2).index, inplace=True)
df.drop(df.tail(1).index, inplace=True)

#removing Nan(Not a number) values (if any) 
df.replace("", np.NaN, inplace=True)

#removing  all empty columns and rows
df.dropna(how="all", axis=1, inplace=True) #axis=1--> columns
df.dropna(how="all", axis=0, inplace=True) #axis=0--> rows
#reset index and header 
df.reset_index(inplace=True,drop=True)
df.columns = np.arange(0, len(df.columns))

print(df)
df.to_csv("report(2).csv", header=None, index=None) #output into a csv file
