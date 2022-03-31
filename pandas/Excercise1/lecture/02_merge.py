import pandas as pd

dfHeight = pd.read_csv("./8842height.phe.txt", sep="\t")
dfKare = pd.read_csv("./KARE.csv", sep=",")

# print(dfKare.count())
# print(dfHeight.count())
dfMerged = pd.merge(dfHeight, dfKare, on="hid")

# print(dfMerged.count())

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()

dfOrder = dfMerged[['id', 'hid','Area', 'Age', 'Sex', 'Height']]
save(dfOrder, "./order.xlsx")

