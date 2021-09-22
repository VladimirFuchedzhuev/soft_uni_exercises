number_of_snowballs = int(input())
snowball_value = 0
highest_snowball_value = 0
highest_snowball_snow = 0
highest_snowball_time = 0
highest_snowball_quality = 0
for ball in range(1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        highest_snowball_snow = snowball_snow
        highest_snowball_time = snowball_time
        highest_snowball_quality = snowball_quality


print(f"{highest_snowball_snow} : {highest_snowball_time} = {int(highest_snowball_value)} ({highest_snowball_quality})")