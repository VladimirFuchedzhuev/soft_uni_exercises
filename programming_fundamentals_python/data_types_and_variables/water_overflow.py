number_of_lines = int(input())
capacity = 255
water = 0

for line in range(number_of_lines):
    liters_of_water = int(input())
    if capacity >= water + liters_of_water:
        water += liters_of_water
    else:
        print("Insufficient capacity!")


print(water)

