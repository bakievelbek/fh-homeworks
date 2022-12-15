# 4. Subtract the mean of each row of a matrix

import numpy as np

a = np.random.rand(3, 4)
print(a)

b = a - a.mean(axis=1, keepdims=True)
print(b)
