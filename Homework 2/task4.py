def convert_into_list(a):
    return [a]


list_of_strings = ['First', 'Second', 'Third', 'Fourth']
result = map(convert_into_list, list_of_strings)
print(list(result))
