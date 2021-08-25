import math


days = int(input())
food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

required_food = (dog_food_per_day + cat_food_per_day + (turtle_food_per_day / 1000)) * days

if food >= required_food:
    food_left = math.floor(food - required_food)
    print(f"{food_left} kilos of food left.")
else:
    needed_food = math.ceil(required_food - food)
    print(f"{needed_food} more kilos of food are needed.")
