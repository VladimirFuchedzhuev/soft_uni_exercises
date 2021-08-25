deposited_sum = float(input())
deposit_term = int(input())
air = float(input())
deposit_air = deposited_sum * air / 100
air_for_month = deposit_air / 12
sum = deposited_sum + (deposit_term * air_for_month)
print(float(sum))