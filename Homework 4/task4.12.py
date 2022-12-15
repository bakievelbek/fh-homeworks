# 5. How to I sort an array by the nth column?

import numpy as np
import random


random_size = random.randint(1, 10)

a = np.random.rand(random_size, random_size)

print(a)

nth_column = random_size - 1

a = a[a[:, nth_column].argsort()]
print(a)

