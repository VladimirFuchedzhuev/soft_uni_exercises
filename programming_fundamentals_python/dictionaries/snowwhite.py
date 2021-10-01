dwarfs, colors = {}, {}

command = input()
while not command == "Once upon a time":
    dwarf, hat_color, physics = command.split(" <:> ")
    physics = int(physics)
    dwarf_key = f"{dwarf}:{hat_color}"

    if dwarf_key not in dwarfs:
        dwarfs[dwarf_key] = [hat_color, physics]

        if hat_color not in colors:
            colors[hat_color] = 0
        colors[hat_color] += 1

    elif dwarfs[dwarf_key][1] < physics:
        dwarfs[dwarf_key][1] = physics

    command = input()

#sorted_dwarfs = {d: i for d, i in sorted(dwarfs.items(), key=lambda x: (-x[1][1], -colors[x[1][0]]))}
sorted_dwarfs = {}
for key, value in sorted(dwarfs.items(), key=lambda x: (-x[1][1], -colors[x[1][0]])):
    sorted_dwarfs.update({key: value})
for key, values in sorted_dwarfs.items():
    name = key.split(":")[0]
    color, physic = values
    print(f"({color}) {name} <-> {physic}")