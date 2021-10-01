data = input()
contest_info = {}
user_book = {}
best_candidate_points = 0
best_candidate = ''
while not data == "end of contests":
    contest, password = data.split(":")
    if contest not in contest_info:
        contest_info[contest] = password

    data = input()

user_data = input()
while not user_data == "end of submissions":
    contest, password, user, points = user_data.split("=>")
    if contest in contest_info:
        if password in contest_info[contest]:
            if user not in user_book:
                user_book[user] = {contest: int(points)}
            else:
                if contest in user_book[user]:
                    if int(points) > user_book[user][contest]:
                        user_book[user][contest] = int(points)
                else:
                    user_book[user][contest] = int(points)

    user_data = input()

for user, value in user_book.items():
    current_points = 0
    for contest, point in value.items():
        current_points += point
        if current_points > best_candidate_points:
            best_candidate = user
            best_candidate_points = current_points

print(f"Best candidate is {best_candidate} with total {best_candidate_points} points.")
print("Ranking:")
for k, v in sorted(user_book.items(), key=lambda x: x[0]):
    print(f"{k}")
    for k_k, v_v in sorted(user_book[k].items(), key=lambda x: -x[1]):
        print(f"#  {k_k} -> {v_v}")
