class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, animal_name):
        if species == "mammal":
            self.mammals.append(animal_name)
        elif species == "fish":
            self.fishes.append(animal_name)
        elif species == "bird":
            self.birds.append(animal_name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fishes":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += print(f"Total animals: {self.__animals}")
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())
for _ in range(count):
    animal = input().split(" ")
    speciess = animal[0]
    animal_name1 = animal[1]
    zoo.add_animal(speciess, animal_name1)

info = input()
print(zoo.get_info(info))
