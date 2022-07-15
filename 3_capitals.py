country_list = input().split(', ')
capitals_list = input().split(', ')
country_capital_dict = {key: value for (key, value) in zip(country_list, capitals_list)}
for key, value in country_capital_dict.items():
    print(f'{key} -> {value}')
#countr_cap_dict = dict(zip(country_list, capitals_list))