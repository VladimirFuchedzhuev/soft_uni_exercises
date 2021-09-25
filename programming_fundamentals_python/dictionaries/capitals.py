country = input().split(", ")
capital = input().split(", ")

for key, value in zip(country, capital):
    print(f"{key} -> {value}")