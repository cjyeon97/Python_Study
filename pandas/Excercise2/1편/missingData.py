import pandas as pd
import numpy as np

dates = pd.date_range('20200411', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df1 = df.reindex(index=dates[0:4], columns=list(df.columns))
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)

droped = df1.dropna(how="any")
print(droped)

filled = df1.fillna(value="멍개")
print(filled)

booleaned = pd.isna(df1)
print(booleaned)