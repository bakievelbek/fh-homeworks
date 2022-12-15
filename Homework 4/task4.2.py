# 2. Create a 5x5 array with random values. and find the minimum and maximum values

import numpy as np
import random
import matplotlib.pyplot as plt

range_ = random.randint(0, 100) * 1000

colors = ['yellow', 'green', 'red', 'blue']

random_number_array = np.random.randint(range_, size=(5, 5))
print("Original Array:")
print(random_number_array)

print("Maximum value:")
print(random_number_array.max(initial=None))

print("Minimum value:")
print(random_number_array.min(initial=None))

print(list(random_number_array[0]))

plt.pie(list(random_number_array[0]), labels=list(random_number_array[0]), colors=colors)
plt.axis('equal')
plt.show()
