destination = input()

while destination != "End":
    min_budget = float(input())
    saved = 0
    while saved < min_budget:
        money = float(input())
        saved += money
    else:
        print(f"Going to {destination}!")
        saved = 0
    destination = input()
