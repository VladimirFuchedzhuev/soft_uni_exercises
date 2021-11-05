population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())
equal_distribution = False
for i in range(len(population)):
    wealthiest = max(population)
    poorest = min(population)
    take_wealth = population.index(wealthiest)
    give_poorest = population.index(poorest)
    population[give_poorest] += minimum_wealth - poorest
    population[take_wealth] -= minimum_wealth - poorest

if min(population) >= minimum_wealth:
    print(population)
else:
    print("No equal distribution possible")