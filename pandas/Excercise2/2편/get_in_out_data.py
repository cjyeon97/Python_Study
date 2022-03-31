import pandas as pd

df = pd.DataFrame({
  "id":[1,2,3,4,5,6], 
  "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']
})

# CSV
df.to_csv('foo.csv') # write
pd.read_csv('foo.csv') # read

# HDF5
df.to_hdf('foo.h5', 'df') # write
pd.read_hdf('foo.h5', 'df') # read

# Excel
df.to_excel('foo.xlsx', sheet_name='Sheet1') # write
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']) # read