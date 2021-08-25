company = input()
adult_tickets = int(input())
kid_tickets = int(input())
adult_tickets_price = float(input())
service_tax = float(input())

kid_tickets_price = adult_tickets_price * 0.3
adult_tickets_price_with_tax = adult_tickets_price + service_tax
kid_tickets_price_with_tax = kid_tickets_price + service_tax
total_tickets_income = adult_tickets * adult_tickets_price_with_tax + kid_tickets * kid_tickets_price_with_tax
profit = total_tickets_income * 0.2

print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")