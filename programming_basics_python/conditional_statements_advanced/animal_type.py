animal_type = input()
species = ""

if animal_type == "dog":
    species = "mammal"
elif animal_type == "crocodile" or animal_type == "tortoise" or animal_type == "snake":
    species = "reptile"
else:
    print("unknown")
print(species)
