input_lines = input()
players_pool = {}
player_skills = {}

while not input_lines == "Season end":
    if "->" in input_lines:
        player, position, skill = input_lines.split(" -> ")
        skill = int(skill)
        if player not in players_pool:
            players_pool[player] = {position: skill}
            player_skills[player] = skill
        else:
            if position not in players_pool[player]:
                players_pool[player][position] = skill
                player_skills[player] += skill

            else:
                if players_pool[player][position] < skill:
                    players_pool[player][position] = skill
                    player_skills[player] += skill - players_pool[player][position]
    elif "vs" in input_lines:
        player_1, player_2 = input_lines.split(" vs ")
        if player_1 in players_pool and player_2 in players_pool:
            player_1_pos = 0
            player_2_pos = 0
            for pos_1 in players_pool[player_1]:
                for pos_2 in players_pool[player_2]:
                    if pos_1 == pos_2:
                        player_1_pos += players_pool[player_1][pos_1]
                        player_2_pos += players_pool[player_2][pos_2]
            if player_1_pos > player_2_pos:
                del players_pool[player_2]
                del player_skills[player_2]
            elif player_2_pos > player_1_pos:
                del players_pool[player_1]
                del player_skills[player_1]
    input_lines = input()

for k, v in sorted(player_skills.items(), key=lambda x: (-x[1], x[0])):
    print(f"{k}: {v} skill")
    for k_k, v_v in sorted(players_pool[k].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {k_k} <::> {v_v}")