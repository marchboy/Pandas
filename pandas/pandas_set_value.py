import pandas as pd
import numpy as np

dates = pd.date_range('20160101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[2,2] = 1111  # 按所在的行号列号筛选
df.loc['2016-01-03', 'D'] = 2222 # 按纯标签名字筛查
df.A[df.A>0] = 0 
df['F'] = np.nan
df['G']  = pd.Series([1,2,3,4,5,6], index=pd.date_range('20160101', periods=6))
print(df)
