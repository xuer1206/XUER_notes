import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(16).reshape((4,4)),index = list(range(4)),columns=['a','b','c','d'])

print(df)
print(df.iloc[:3,[0,1,-1]])