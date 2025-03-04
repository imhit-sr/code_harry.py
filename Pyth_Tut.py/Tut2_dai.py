# Explanation of Each Method
# Method	Function	Example
# sum()	Counts True values (since True = 1, False = 0).	np.array([True, False, True]).sum() → 2
# any()	Returns True if at least one element is True.	np.array([False, False, True]).any() → True
# all()	Returns True if all elements are True.	np.array([True, True, False]).all() → False

# Q.3 Methods for boolean in numpy array. Choose the relevant from the following options.
# (a) sum(), any(), np.type()
# (b) sum(), any(), all(), np.type()
# (c) objects(), any()
# (d) sum(), any(), all()
# import numpy as np
# arr = np.array([1,4,5,6,86])
# index = np.where(arr == 86)
# print(index)

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 6])

result = np.setdiff1d(arr1, arr2)
print(result) 

# What will be the output of following program:
#  import numpy as np
#  a=np.array([4,5,6])
#  b=a
#  a[1]=3
#  print(b)