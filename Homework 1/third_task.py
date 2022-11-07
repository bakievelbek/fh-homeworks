string = input("Enter string to count vowels: ")
vowels = ['a', 'o', 'u', 'e', 'i']
vowel_counter = 0
for vowel in string.lower():
    if vowel in vowels:
        vowel_counter += 1
print(f"The number of vowels in {string} is {vowel_counter}")
