#coding = utf-8

import numpy as np
import pandas as pd

dates = pd.date_range('20160101', periods=6)

df = pd.DataFrame(np.arange(24).reshape((6,4)), index = dates, columns=['A','B','C','D'])

print(df['A'], df.A)
print(df[0:3], df['20160101':'20160103'])

##select by label:(loc, pandas) 按纯标签名字筛查
print(df.loc['20160102'])
print(df.loc[:,['A','B']])
print(df.loc['20160102',['A','B']])

##select by positoin:iloc 按所在的行号列号筛选
print(df.iloc[3:5,1:3])

##mixed selection:ix 按标签和位置号码综合一起筛选
print(df.ix[:3,['A','C']])

##Booling indexing 是或否的帅选
print(df[df.A > 8])
