command = input()
dictionary = {}
counter = 0
key = 0
value = 0
while not command == 'stop':
    counter += 1
    if counter % 2 == 1:
        key = command
    else:
        value = int(command)
        if key not in dictionary:
            dictionary[key] = value
            value = 0
        dictionary[key] += value
    command = input()
for key, value in dictionary.items():
    print(f'{key} -> {value}')




