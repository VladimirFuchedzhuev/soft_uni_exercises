students = int(input())
grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0
average_grade = 0

for student in range(0, students):
    student_grade = float(input())
    if 2 <= student_grade <= 2.99:
        grade_d += 1
        average_grade += student_grade
    elif 3 <= student_grade <= 3.99:
        grade_c += 1
        average_grade += student_grade
    elif 4 <= student_grade <= 4.99:
        grade_b += 1
        average_grade += student_grade
    elif student_grade >= 5:
        grade_a += 1
        average_grade += student_grade

print(f"Top students: {((grade_a / students) * 100):.2f}%")
print(f"Between 4.00 and 4.99: {((grade_b / students) * 100):.2f}%")
print(f"Between 3.00 and 3.99: {((grade_c / students) * 100):.2f}%")
print(f"Fail: {((grade_d / students) * 100):.2f}%")
print(f"Average: {(average_grade / students):.2f}")