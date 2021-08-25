juniors = int(input())
seniors = int(input())
type_race = input()
juniors_ticket = 0
seniors_ticket = 0
income = 0

if type_race == "trail":
    juniors_ticket = 5.5
    seniors_ticket = 7
    income = juniors * juniors_ticket + seniors * seniors_ticket
elif type_race == "cross-country":
    junior_ticket = 8
    seniors_ticket = 9.5
    income = juniors * junior_ticket + seniors * seniors_ticket
    if juniors + seniors >= 50:
        income *= 0.75
elif type_race == "downhill":
    junior_ticket = 12.25
    seniors_ticket = 13.75
    income = juniors * junior_ticket + seniors * seniors_ticket
elif type_race == "road":
    junior_ticket = 20
    seniors_ticket = 21.5
    income = juniors * junior_ticket + seniors * seniors_ticket
donation = income * 0.95
print(f"{donation:.2f}")
