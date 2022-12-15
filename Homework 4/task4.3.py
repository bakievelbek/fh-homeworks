# 3. Normalize a 5x5 random matrix

import numpy as np
import random

range_ = random.randint(0, 100) * 1000

random_number_array = np.random.randint(range_, size=(5, 5))
print("Original Array:")
print(random_number_array)

print("Maximum value:")
xmax = random_number_array.max(initial=None)
print(xmax)

print("Minimum value:")
xmin = random_number_array.min(initial=None)
print(xmin)

normalized_array = (random_number_array - xmin) / (xmax - xmin)
print(normalized_array)
