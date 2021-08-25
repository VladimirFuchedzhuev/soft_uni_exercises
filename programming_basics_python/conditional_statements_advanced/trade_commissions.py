city = input()
sells = float(input())

commission = 0

if sells > 10000:
    if city == "Sofia":
        commission = sells * 0.12
    elif city == "Varna":
        commission = sells * 0.13
    elif city == "Plovdiv":
        commission = sells * 0.145
elif sells > 1000:
    if city == "Sofia":
        commission = sells * 0.08
    elif city == "Varna":
        commission = sells * 0.10
    elif city == "Plovdiv":
        commission = sells * 0.12
elif sells > 500:
    if city == "Sofia":
        commission = sells * 0.07
    elif city == "Varna":
        commission = sells * 0.075
    elif city == "Plovdiv":
        commission = sells * 0.08
elif sells >= 0:
    if city == "Sofia":
        commission = sells * 0.05
    elif city == "Varna":
        commission = sells * 0.045
    elif city == "Plovdiv":
        commission = sells * 0.055

if commission == 0:
    print("error")
else:
    print(f"{commission:.2f}")

