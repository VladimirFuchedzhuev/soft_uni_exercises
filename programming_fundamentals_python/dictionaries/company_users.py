command = input()


company_info = {}



while not command == "End":
    company_name, employee_id = command.split(' -> ')

    if company_name not in company_info:
        company_info[company_name] = []

    if employee_id not in company_info[company_name]:
        company_info[company_name].append(employee_id)

    command = input()

for company, employee_id in sorted(company_info.items(), key=lambda x: x[0]):
    print(company)
    for employee in employee_id:
        print(f'-- {employee}')