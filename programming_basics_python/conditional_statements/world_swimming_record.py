import math


record = float(input())
distance = float(input())
time_per_meter = float(input())


swim_time = distance * time_per_meter
delay = math.floor(distance / 15) * 12.5
total_time = swim_time + delay


if total_time < record:
    print (f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    difference = total_time - record
    print(f"No, he failed! He was {difference:.2f} seconds slower.")

