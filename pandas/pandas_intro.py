# based on py3.x

import pandas as pd
import numpy as np


s = pd.Series([1,2,3,np.nan,5,6])
print(s)

dates = pd.date_range('20160701',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=['a','b','c','d'])
df

