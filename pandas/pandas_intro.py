#based on py3.x

import pandas as pd
import numpy as np

s = pd.Series([1,2,3,np.nan,5,6])
print(s)

dates = pd.date_range('20160701',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=['a','b','c','d'])
df['b']

df1 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'})

print(df2)
print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
print(df.T)

print(df2.sort_index(axis=1, ascending=False))
print(df2.sort_index(axis=0, ascending=False))

print(df2.sort_values(by = 'E'))







