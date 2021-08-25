holiday = int(input())

workind_days = 365 - holiday
holiday_minutues = holiday * 127
workind_day_minutes = workind_days * 63
total_play_time = holiday_minutues + workind_day_minutes
time = abs(30000 - total_play_time)
h = time // 60
m = time % 60


if total_play_time < 30000:
    print("Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")
else:
    print("Tom will run away")
    print(f"{h} hours and {m} minutes more for play")