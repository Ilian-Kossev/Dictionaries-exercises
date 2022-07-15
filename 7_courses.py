register = {}
command = input()
while not command == 'end':
    course_name, student_name = command.split(' : ')
    if course_name not in register:
        register[course_name] = []
    register[course_name].append(student_name)
    command = input()

sorted_reg = dict(sorted(register.items(), key=lambda x: -len(x[1])))
for key, value in sorted_reg.items():
    print(f'{key}: {len(sorted_reg[key])}')
    value.sort()
    for item in value:
        print(f'-- {item}')




