balls = int(input())
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_colors = 0
total_points = 0
black_balls = 0


for colored in range(1, balls + 1):
    ball_color = input()
    if ball_color == "red":
        total_points += 5
        red_balls += 1
    elif ball_color == "orange":
        total_points += 10
        orange_balls += 1
    elif ball_color == "yellow":
        total_points += 15
        yellow_balls += 1
    elif ball_color == "white":
        total_points += 20
        white_balls += 1
    elif ball_color == "black":
        total_points //= 2
        black_balls += 1
    else:
        other_colors += 1


print(f"Total points: {total_points}")
print(f"Points from red balls: {red_balls}")
print(f"Points from orange balls: {orange_balls}")
print(f"Points from yellow balls: {yellow_balls}")
print(f"Points from white balls: {white_balls}")
print(f"Other colors picked: {other_colors}")
print(f"Divides from black balls: {black_balls}")
