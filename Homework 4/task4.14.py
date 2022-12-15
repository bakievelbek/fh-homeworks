# 7. Consider a 16x16 array, how to get the block-sum (block size is 4x4)

import numpy as np

array1 = np.random.rand(16, 16)
k = 5
print("Original arrays:")
print(array1)
result = np.add.reduceat(np.add.reduceat(array1, np.arange(0, array1.shape[0], k), axis=0),
                         np.arange(0, array1.shape[1], k), axis=1)

print("\nBlock-sum  of the 16x16 array:")

print(result)

print("\nSize: ")

print(str(len(result)) + "x" + str(len(result)))
