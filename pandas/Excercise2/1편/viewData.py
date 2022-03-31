import pandas as pd
import numpy as np

dates = pd.date_range('20200411', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

print(df.head())
print(df.tail(3))

print(df.index)
print(df.columns)

print(df.to_numpy())

df2 = pd.DataFrame({
  'A': 1.,
  'B': pd.Timestamp('20130102'),
  'C': pd.Series(1, index=list(range(4)), dtype='float32'),
  'D': np.array([3] * 4, dtype='int32'),
  'E': pd.Categorical(["test", "train", "test", "train"]),
  'F': 'foo'
})
print(df2.to_numpy())

print(df.describe())

print('전치전')
print(df)
print('전치후')
print(df.T)

sorted_df =df.sort_index(axis=1, ascending=True)
print(sorted_df)

sorted_df = df.sort_values(by='A')
print(sorted_df)