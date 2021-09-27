input_line = input()
ranking = {}


while not input_line == "no more time":
    user, contest, points = input_line.split(" -> ")
    if contest not in ranking:
        ranking[contest] = {user: int(points)}
    else:
        if user not in ranking[contest]:
            ranking[contest][user] = int(points)
        else:
            if ranking[contest][user] < int(points):
                ranking[contest][user] = int(points)

    input_line = input()


total_points = {}
for contest, value in ranking.items():
    for user, points in value.items():
        if user not in total_points:
            total_points[user] = points
        else:
            total_points[user] += points
for contest, value in ranking.items():
    print(f"{contest}: {len(ranking[contest])} participants")
    position = 1
    for user, points in sorted(value.items(), key=lambda x: (-x[1], x[0])):

        print(f"{position}. {user} <::> {points}")
        position += 1
print("Individual standings:")
position = 1
for user, points in sorted(total_points.items(), key=lambda x: (-x[1], x[0])):

    print(f"{position}. {user} -> {points}")
    position += 1