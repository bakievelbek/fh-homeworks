occurrences = {}


def num_of_words(sentence):
    words = sentence.lower().split()
    for word in words:
        if word in occurrences:
            occurrences[word] += 1
        else:
            occurrences[word] = 1


f_string = ''

num_of_words(input("Enter your string: "))
for key in occurrences:
    f_string += f'{key} = {occurrences[key]}, '

print(f_string)
