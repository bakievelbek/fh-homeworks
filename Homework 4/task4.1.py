# 1. Create a vector with values ranging from 10 to 49. Reverse a vector (first element becomes last)

import numpy as np

python_array = [i for i in range(10, 50)]

numpy_array = np.array(python_array)

result = np.flip(numpy_array)

print(result)
