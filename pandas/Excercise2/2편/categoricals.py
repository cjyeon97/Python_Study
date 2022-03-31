import pandas as pd
import numpy as np

df = pd.DataFrame({
  "id":[1,2,3,4,5,6], 
  "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']
})

df["grade"] = df["raw_grade"].astype("category")
df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df)
print(df['grade'])


df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print(df['grade'])

print(df.sort_values(by="grade"))

print(df.groupby("grade").size())