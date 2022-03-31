import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4))
print(df)

# merge
pieces = [df[:3], df[3:7], df[7:]]
merged_df = pd.concat(pieces)
print(merged_df)

# join
## ex1
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

print(left)
print(right)

joined_df = pd.merge(left, right, on='key')
print(joined_df)

## ex2
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})

joined_df = pd.merge(left, right, on='key')
print(joined_df)


# append
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
s = df.iloc[3]
appended_df = df.append(s, ignore_index=True)
print(df)
print(appended_df)