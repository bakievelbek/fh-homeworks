def get_name():
    return input("Please, enter you first and last name: \n")


full_name = get_name()
if ' ' not in full_name or not full_name:
    print('Your first and last names are not separated with a space or empty')

else:
    name_array = full_name.split(' ')
    reversed_array = name_array[::-1]
    reversed_name = ' '.join(reversed_array)
    print(reversed_name)
