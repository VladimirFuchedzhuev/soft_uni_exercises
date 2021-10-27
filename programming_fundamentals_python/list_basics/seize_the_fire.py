cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
cell_values = []
for cell in cells:
    current_cell = cell.split(" = ")
    type_of_fire = current_cell[0]
    cell_fire = int(current_cell[1])
    if type_of_fire == "High":
        if not 81<= cell_fire <= 125:
            continue
    elif type_of_fire == "Medium":
        if not 51 <= cell_fire <= 80:
            continue
    elif type_of_fire == "Low":
        if not 1 <= cell_fire <= 50:
            continue
    if water < cell_fire:
        continue
    cell_values.append(cell_fire)
    effort += cell_fire * 0.25
    water -= cell_fire
    total_fire += cell_fire

print("Cells:")
for value in cell_values:
    print(f" - {value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")



