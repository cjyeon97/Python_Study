import pandas as pd
import numpy as np

dates = pd.date_range('20200411', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

# selection by label
print(df['A']) # df.A
print(df.loc[dates[0]])
print(df.loc[:, ['A', 'B']])

print(df.loc['20200411':'20200414', ['A', 'B']])

print(df.loc['20200411', ['A', 'B']])

print(df.loc[dates[0], 'A'])
print(df.at[dates[0], 'A'])

# selection by position
print(df.iloc[3])

print(df.iloc[3:5, 0:2])
print(df.iloc[1:3, :])
print(df.iloc[:, 1:3])
print(df.iloc[1, 1])
print(df.iat[1, 1])

# Boolean indexing
print(df[df['A'] > 0])

print(df[df > 0])

df2 = df.copy() # 데이터 딥 카피
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
print(df2[df2['E'].isin(['two', 'four'])])

# setting
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20200411', periods=6))
print(s1)
df['F'] = s1
print(df)

df.at[dates[0], 'A'] = 0
df.iat[0, 1] = 0
df.loc[:, 'D'] = np.array([5] * len(df))
print(df)

df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)