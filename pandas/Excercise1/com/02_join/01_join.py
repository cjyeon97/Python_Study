import pandas as pd

dfHeight = pd.read_csv("./8842height.phe.txt", sep="\t")
dfKare = pd.read_csv("./KARE.csv", sep=",")

dfMerged = pd.merge(dfHeight, dfKare, on="hid")

print(dfMerged[['hid', 'Height', 'Age', 'Sex']])
