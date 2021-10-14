first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
people_count = int(input())

people_per_hour = first_employee + second_employee + third_employee
hours = 0

while people_count > 0:
    hours += 1
    people_count -= people_per_hour

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")