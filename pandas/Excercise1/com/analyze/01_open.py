import pandas as pd
import json
df = pd.read_json("/Users/kyeongrok/Desktop/result.json")

authors = df['authors']

count = 0
authorItems = []
for authorList in authors:
    count = count + len(authorList)
    authorItems = authorItems + authorList


file = open("/Users/kyeongrok/Desktop/authors.json", "w+")
file.write(json.dumps(authorItems))
