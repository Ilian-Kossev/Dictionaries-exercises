input_list = input().split()
dictionary = {}
key = 0
value = 0
for num in range(0, len(input_list), 2):
    value = int(input_list[num])
    key = input_list[num + 1].lower()
    if key not in dictionary.keys():
        dictionary[key] = 0
    dictionary[key] += value

for key in dictionary:
    if key == 'shards' and dictionary[key] >= 250:
        print('Shadowmourne obtained!')
        dictionary[key] -= 250
    elif key == 'fragments' and dictionary[key] >= 250:
        print('Valanyr obtained!')
        dictionary[key] -= 250
    elif key == 'motes' and dictionary[key] >= 250:
        print('Dragnowrath obtained!')
        dictionary[key] -= 250
dict_valuables = {key: value for (key, value) in dictionary.items() if key == 'shards' or key == 'fragments' or key == 'motes'}
dict_junk = {key: value for (key, value) in dictionary.items() if not key == 'shards' and not key == 'fragments' and not key == 'motes'}
sorted_dict_valuables = dict(sorted(dict_valuables.items(), key=lambda x: x[1], reverse=True))
sorted_dict_junk = dict(sorted(dict_junk.items(), key=lambda x: x[1], reverse=True))
for key, value in sorted_dict_valuables.items():
    print(f'{key}: {value}')
for key, value in sorted_dict_junk.items():
    print(f'{key}: {value}')



