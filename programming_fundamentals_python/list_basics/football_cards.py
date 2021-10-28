cards_list = input().split(" ")
team_a = []
team_b = []
game_is_ended = False

for i in range(1, 12):
    team_a.append(f"A-{i}")
for i in range(1, 12):
    team_b.append(f"B-{i}")

for card in cards_list:
    if card in team_a:
        team_a.remove(card)
    elif card in team_b:
        team_b.remove(card)
    if len(team_a) < 7 or len(team_b) < 7:
        game_is_ended = True
        break

if game_is_ended:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    print("Game was terminated")
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
