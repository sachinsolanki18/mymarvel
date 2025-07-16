import pandas as pd
import numpy as np
# From a NumPy array
np_arr = np.array([10, 20, 30, 40])
s1 = pd.Series(np_arr)
print("Series from NumPy array:\n", s1)
print("Index of s1:", s1.index)
print("Values of s1:", s1.values)
s2 = pd.Series(np_arr, index=['a', 'b', 'c', 'd'])
print("\nSeries with custom index:\n", s2)
