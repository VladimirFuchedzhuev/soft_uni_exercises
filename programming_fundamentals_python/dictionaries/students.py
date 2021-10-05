data = input()
courses = {}

while ':' in data:
    student_name, id, course_name = data.split(":")
    if course_name not in courses:
        courses[course_name] = {}
    courses[course_name][id] = student_name

    data = input()
searched_course = data.split("_")

searched_course_as_list = " ".join(searched_course)

for course_name in courses:
    if course_name == searched_course_as_list:
        for id, name in courses[course_name].items():
            print(f"{name} - {id}")