# 4. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)

import numpy as np
import random

range_ = random.randint(0, 100) * 1000

random_number_array_1 = np.random.randint(range_, size=(5, 3))
random_number_array_2 = np.random.randint(range_, size=(3, 2))

print(np.matmul(random_number_array_1, random_number_array_2))

