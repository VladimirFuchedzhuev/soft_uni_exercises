from math import floor


required_hours = int(input())
available_days = int(input())
employees = int(input())

available_hours = (available_days * 0.9) * 8
overtime_hours = employees * 2 * available_days
total_hours = available_hours + overtime_hours

if total_hours >= required_hours:
    hours_left = floor(total_hours) - required_hours
    print(f"Yes!{hours_left} hours left.")
else:
    hours_needed= required_hours - floor(total_hours)
    print(f"Not enough time!{hours_needed} hours needed.")
