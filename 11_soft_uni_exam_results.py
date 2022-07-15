submissions_list = {}
submission_count = {}

command = input()
while not command == 'exam finished':
    if 'banned' not in command:
        student_name, course, points = command.split('-')
        if course not in submissions_list:
            submissions_list[course] = {}
            submission_count[course] = 0
        if student_name not in submissions_list[course]:
            submissions_list[course][student_name] = int(points)
        if int(points) <= submissions_list[course][student_name]:
            submission_count[course] += 1
            command = input()
            continue
        else:
            submissions_list[course][student_name] = int(points)
            submission_count[course] += 1
    else:
        student_name, action = command.split('-')
        for key in submissions_list:
            if student_name in submissions_list[key]:
                del submissions_list[key][student_name] # submissions_list[key]pop.(student_name)

    command = input()
final_register = {}
for key in submissions_list:
    for nested_key, nested_value in submissions_list[key].items():
        new_key = nested_key
        new_value = nested_value
        final_register[new_key] = nested_value
print('Results:')
for (key, value) in sorted(final_register.items(), key=lambda x: (-x[1], x[0])):
    print(f'{key} | {value}')

print('Submissions:')
for (key, value) in sorted(submission_count.items(), key=lambda x: x[0]):
    print(f'{key} - {value}')