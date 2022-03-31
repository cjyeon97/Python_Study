import pandas as pd
import numpy as np

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
print(tuples)

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]

print(df2)

# stack

stacked = df2.stack()
print(stacked)

unstacked1 = stacked.unstack()
print(unstacked1)

unstacked2 = stacked.unstack(1)

# pivot tables

df = pd.DataFrame({
  'A' : ['one', 'one', 'two', 'three'] * 3,
  'B' : ['A', 'B', 'C'] * 4,
  'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
  'D' : np.random.randn(12),
  'E' : np.random.randn(12)
})
print(df)

pivot_table = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
print(pivot_table)
