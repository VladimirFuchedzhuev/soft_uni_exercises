vegies = float(input())
fruits = float(input())
total_vegies_kg = int(input())
total_fruits_kg = int(input())

total_income = (vegies * total_vegies_kg + fruits * total_fruits_kg) / 1.94
print(f"{total_income:.2f}")