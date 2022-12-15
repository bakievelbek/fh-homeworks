# 2. Consider two random array A and B, check if they are equal

import numpy as np
import matplotlib.pyplot as plt

random_number_array_1 = np.random.rand(3)
random_number_array_2 = np.random.rand(3)

print(random_number_array_1)
print(random_number_array_2)

print(np.array_equal(random_number_array_1, random_number_array_2))

plt.bar(random_number_array_1, random_number_array_2)
plt.show()
