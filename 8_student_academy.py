student_name = ''
student_grade = 0
student_register = {}
number = int(input())
for num in range(number * 2):
    if num % 2 == 0:
        student_name = input()
    else:
        student_grade = float(input())
    if student_name not in student_register:
        student_register[student_name] = []
    student_register[student_name].append(student_grade)
    student_grade = 0
final_register = {}
for key, value in student_register.items():
    student_average_grade = sum(value) / (len(value) / 2)
    if student_average_grade < 4.5:
        continue
    else:
        final_register[key] = student_average_grade

sorted_register = dict(sorted(final_register.items(), key=lambda x: -x[1]))
for key, value in sorted_register.items():
    print(f'{key} -> {value:.2f}')

