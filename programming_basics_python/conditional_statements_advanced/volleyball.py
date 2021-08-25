from math import floor
year = input()
holidays = int(input())
weekends_outside = int(input())

weekends_per_year = 48
weekends_in_sofia = weekends_per_year - weekends_outside
weekends_games_in_sofia = weekends_in_sofia * 3 / 4
weekend_games_outside = weekends_outside
holidays_games_in_sofia = holidays * 2 / 3
total_games = weekends_games_in_sofia + weekends_outside + holidays_games_in_sofia


if year == "leap":
    total_games *= 1.15
    print(floor(total_games))
else:
    print(floor(total_games))