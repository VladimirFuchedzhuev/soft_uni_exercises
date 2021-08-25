failed_threshold = int(input())
problems_counter = 0
counter_bad_grades = 0
sum_grades = 0
last_problem = ""
has_failed = True

while counter_bad_grades < failed_threshold:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        counter_bad_grades += 1
    sum_grades += grade
    problems_counter += 1
    last_problem = problem_name
if has_failed:
    print(f"You need a break, {counter_bad_grades} poor grades.")
else:
    print(f"Average score: {sum_grades /problems_counter:.2f}")
    print(f"Number of problems: {problems_counter}")
    print(f"Last problem: {last_problem}")