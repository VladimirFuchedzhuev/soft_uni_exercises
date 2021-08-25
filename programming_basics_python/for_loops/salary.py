tabs = int(input())
salary = int(input())
fine = 0
for i in range(1, tabs + 1):
    page = input()
    if page == "Facebook":
        fine += 150
    elif page == "Instagram":
        fine += 100
    elif page == "Reddit":
        fine += 50

if salary > fine:
    total_salary_left = salary - fine
    print(total_salary_left)
else:
    print("You have lost your salary." )