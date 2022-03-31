import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

df = pd.DataFrame(
  np.random.randn(1000, 4), 
  index=ts.index,
  columns=['A', 'B', 'C', 'D']
) 

df = df.cumsum()
df.plot(); 

plt.figure(); 
plt.legend(loc='best')
plt.show()