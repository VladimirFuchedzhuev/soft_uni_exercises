students = int(input())
course_lectures = int(input())
additional_bonus = int(input())


student_list = []

best_student = 0
for student in range(students):
    student_attendances = int(input())
    total_bonus = student_attendances / course_lectures * (5 + additional_bonus)
    student_list.append(total_bonus)
