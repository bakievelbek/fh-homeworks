# 6. Compute a matrix rank

import numpy as np
import random

range_ = random.randint(0, 10)

random_number_array = np.random.randint(range_, size=(range_, range_))
print(random_number_array)

print("The Rank of a Matrix: ", np.linalg.matrix_rank(random_number_array))
