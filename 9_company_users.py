register = {}
command = input()
while not command == 'End':
    company_name, employee_id = command.split(' -> ')
    if company_name not in register:
        register[company_name] = []
    if employee_id not in register[company_name]:
        register[company_name].append(employee_id)
    command = input()
sorted_register = dict(sorted(register.items(), key=lambda x: x[0]))
for key in sorted_register:
    print(key)
    for element in sorted_register[key]:
        print(f'-- {element}')
