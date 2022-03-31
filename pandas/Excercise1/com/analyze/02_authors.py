import pandas as pd
df = pd.read_json("./authors.json")

for item in df[0]:
    print(len(item.split(", ")))
