hour = int(input())
minutes = int(input())

time = hour * 60 + minutes
time_after_15_min = time + 15

total_hours = time_after_15_min // 60
total_minutes = time_after_15_min % 60


if total_hours == 24:
    total_hours = 0
if total_minutes < 10:
    print(f"{total_hours}:0{total_minutes}")
else:
    print(f"{total_hours}:{total_minutes}")
