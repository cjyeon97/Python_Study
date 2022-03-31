import pandas as pd
import numpy as np

dates = pd.date_range('20200411', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

# stats
print(df.mean())

print(df.mean(1))

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)

a = df.sub(s, axis='index')
print(a)

# apply
sumed = df.apply(np.cumsum)
print(sumed)
mined = df.apply(lambda x: x.max() - x.min())
print(mined)

# histogram
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)

print(s.value_counts())

# string method
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())