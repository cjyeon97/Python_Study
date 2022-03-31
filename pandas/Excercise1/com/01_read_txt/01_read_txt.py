import pandas as pd

df = pd.read_csv("./8842height.phe.txt", sep="\t")

print(df.count())
