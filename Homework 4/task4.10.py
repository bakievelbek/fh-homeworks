# 3. Consider a random vector with shape (100,2) representing coordinates, find point by point distances

import numpy as np

a = np.random.random((100, 2))
x, y = np.atleast_2d(a[:, 0], a[:, 1])
d = np.sqrt((x - x.T) ** 2 + (y - y.T) ** 2)
print(d)
