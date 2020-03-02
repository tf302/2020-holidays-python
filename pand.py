import pandas as  pd
import numpy as np
s = pd.Series([2,5,8,9])
#print(s)
#创建框架
df = pd.DataFrame(np.random.randn(4,4),index=s,columns=s)
print(df)