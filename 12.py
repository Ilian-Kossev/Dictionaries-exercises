data = {}
course_data = input()

while ':' in course_data:
    student, id, course = course_data.split(':')
    if course not in data:
        data[course] = {}
    data[course][student] = id
    course_data = input()

course = course_data.split('_')
final_course = ' '.join(course)
for key in data:
    if key == final_course:
        for k, v in data[key].items():
            print(f'{k} - {v}')


