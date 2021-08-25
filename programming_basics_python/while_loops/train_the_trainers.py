jury = int(input())
command = input()
final_grade = 0
grade_counter = 0
while command != "Finish":
    presentation_grade = 0
    for grade in range(1, jury + 1):
        new_grade =  float(input())
        presentation_grade += new_grade
        final_grade += new_grade
        grade_counter += 1
    average_presentation_grade = presentation_grade / jury
    print(f"{command} - {average_presentation_grade:.2f}.")
    command = input()
average_final_grade = final_grade / grade_counter
print(f"Student's final assessment is {average_final_grade:.2f}.")
