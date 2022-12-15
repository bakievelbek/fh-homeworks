# 1. Consider a generator function that generates 10 integers and use it to build an array

import numpy as np
import random


def generate():
    for n in range(10):
        yield random.randint(1, 10)


nums = np.fromiter(generate(), dtype=float, count=-1)
print("New array:")
print(nums)
