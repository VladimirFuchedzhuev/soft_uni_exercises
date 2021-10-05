n = int(input())
students = {}

for i in range(n):
    student_name = input()
    student_grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(student_grade)

students_above_average = {}
for key, value in students.items():
    if sum(value) / len(value) >= 4.5:
        students_above_average[key] = sum(value) / len(value)

sorted_students = sorted(students_above_average.items(), key=lambda kvp: -kvp[1])

for student_name, grade in sorted_students:
    print(f'{student_name} -> {grade:.2f}')