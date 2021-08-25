player_name = input()
most_goals = 0
best_player = ""
hat_trick = False
while player_name != "END":
    goals = int(input())
    if goals > most_goals:
        most_goals = goals
        best_player = player_name
        if most_goals >= 3:
            hat_trick = True
    if goals >= 10:
        break
    player_name = input()

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")