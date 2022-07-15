input_string = input().split()
string_without_spaces = ''.join(input_string)
dictionary = {}
for letter in string_without_spaces:
    if letter not in dictionary:
        dictionary[letter] = 0
    dictionary[letter] += 1
for key, value in dictionary.items():
    print(f'{key} -> {value}')

