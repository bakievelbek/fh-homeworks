# First 'manual' method

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sample_list_2 = []

for i in range(len(sample_list), 0, -1):
    for element in sample_list:
        if element[-1] == i:
            sample_list_2.insert(0, element)

print(sample_list_2)

# Second method using Lambda

print(sorted(sample_list, key=lambda item: item[1]))
