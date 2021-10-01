lines = input()
users = {}
submissions = {}

while not lines == "exam finished":
    data = lines.split("-")
    if "banned" not in data:
        user_name = data[0]
        language = data[1]
        points = int(data[2])
        if user_name not in users:
            users[user_name] = points
        else:
            if users[user_name] < points:
                users[user_name] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
    else:
        user_name = data[0]
        users.pop(user_name)

    lines = input()


print("Results:")
[print(f"{key} | {value}") for key, value in sorted(users.items(), key=lambda x: (-x[1], x[0]))]
print("Submissions:")
[print(f"{key} - {value}") for key, value in sorted(submissions.items(), key=lambda x: (-x[1], x[0]))]
