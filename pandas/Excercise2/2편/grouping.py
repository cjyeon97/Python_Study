import pandas as pd
import numpy as np

df = pd.DataFrame({
  'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
  'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
  'C' : np.random.randn(8),
  'D' : np.random.randn(8)
})

grouped1 = df.groupby('A').sum()

grouped2 = df.groupby(['A', 'B']).sum()

print(grouped1)
print(grouped2)