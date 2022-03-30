import pandas as pd

df = pd.read_csv("./KARE.csv", sep=",")

print(df.count())
