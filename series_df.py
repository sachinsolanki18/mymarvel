import numpy as np
import  pandas as pd
#from a nd array
num_arr=np.array([10,20,30,40,50])
print(num_arr)
print("series from num_arr:",pd.Series(num_arr))
#from dict
data_dict={"a":10,"b":30,"c":40}
print(data_dict)
print("series from data_dict:",pd.Series(data_dict))
s3=pd.Series(data_dict,index=['a','b','c','d'])
print(s3)
#From a scalar value: If a scalar value is provided, it will be repeated to match the length of the index.
s4 = pd.Series(8, index=[0, 1, 2, 3,4])
print("\nSeries from scalar:\n", s4)
#head & tail function
long_series = pd.Series(np.arange(0, 100))
print("\nLong Series Head:\n", long_series.head())
print("\nLong Series Tail (last 3 elements):\n", long_series.tail(3))
