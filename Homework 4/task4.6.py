# 6. Extract the integer part of a random array using 5 different methods

import numpy as np

Z = np.random.uniform(0, 10, 10)
print('Z:\n', Z)
print(Z - Z % 1)
print(np.floor(Z))
print(np.ceil(Z) - 1)
print(Z.astype(int))
print(np.trunc(Z))
