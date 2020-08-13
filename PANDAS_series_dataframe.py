import numpy as np
import pandas as pd

np_arr=np.random.rand(3)
pd_series=pd.Series(np.random.rand(3),index=['Row 1','Row 2','Row 3'])
pd_dataframe=pd.DataFrame(np.random.rand(3,2),index=['Row 1','Row 2','Row 3'])
pd_dataframe.columns=['Column 1','Column 2']
print('Numpy array = ',np_arr)
print('PANDA Series :\n',pd_series)
print('PANDA series index objects = ',pd_series.index)
print('\n\nPANDA DataFrame :\n',pd_dataframe)
print('PANDA DataFrame index objects = ',pd_dataframe.index)
print('PANDA DataFrame column objects = ',pd_dataframe.columns)
