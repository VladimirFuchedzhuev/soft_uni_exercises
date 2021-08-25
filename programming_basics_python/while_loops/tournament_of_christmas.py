days = int(input())
donation = 0
days_win = 0
days_lose = 0
for day in range(1, days + 1):
    game = input()
    win = 0
    lose = 0
    donation_for_a_day = 0
    while game != "Finish":
        result =  input()
        if result == "win":
            win += 1
            donation_for_a_day += 20
        else:
            lose += 1
        game = input()
    if win > lose:
        donation_for_a_day *= 1.1
        days_win += 1
    else:
        days_lose += 1
    donation += donation_for_a_day

if days_win > days_lose:
    donation *= 1.2
    print(f"You won the tournament! Total raised money: {donation:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {donation:.2f}")