command = input()
target_steps = 10000
total_steps = 0
while command != "Going home":
    total_steps += int(command)
    if total_steps >= 10000:
        break
    command = input()
else:
    steps_to_home = int(input())
    total_steps += steps_to_home
steps= total_steps - target_steps
if total_steps >= target_steps:
    print(f"Goal reached! Good job!")
    print(f"{steps} steps over the goal!")
else:
    print(f"{abs(steps)} more steps to reach goal.")