fats = int(input())
proteins = int(input())
carbohydrates = int(input())
calories = int(input())
water_in_food = int(input())

grams_fats = ((fats / 100) * calories) / 9
grams_proteins = ((proteins / 100) * calories) / 4
grams_carbohydrates = ((carbohydrates / 100) * calories) / 4

food_weight = grams_fats + grams_proteins + grams_carbohydrates
calories_per_gram = calories / food_weight

water_in_food_per_gram = (100 - water_in_food) / 100
clear_calories_per_gram = water_in_food_per_gram * calories_per_gram

print(f"{clear_calories_per_gram:.4f}")