def symbol_checker(symbol, left_half, right_half):
    left_symbol_count = 0
    right_symbol_count = 0
    max_left_symbol_count = 0
    max_right_symbol_count = 0

    for x in left_half:
        if x == symbol:
            left_symbol_count += 1
            if left_symbol_count >= 6:
                max_left_symbol_count = left_symbol_count
        else:
            left_symbol_count = 0

    for z in right_half:
        if z == symbol:
            right_symbol_count += 1
            if right_symbol_count >= 6:
                max_right_symbol_count = right_symbol_count
        else:
            right_symbol_count = 0

    min_symbols = min(max_left_symbol_count, max_right_symbol_count)

    if min_symbols >= 6:
        if min_symbols == 10:
            print(f'ticket "{col}" - {min_symbols}{symbol} Jackpot!')
        else:
            print(f'ticket "{col}" - {min_symbols}{symbol}')
    else:
        print(f'ticket "{col}" - no match')


collection = [t.strip() for t in input().split(",") if not t.isspace()]

for col in collection:
    if len(col) == 20:
        left_half = col[:10]
        right_half = col[10:]

        if "$" * 6 in left_half and "$" * 6 in right_half:
            symbol = "$"
            symbol_checker(symbol, left_half, right_half)

        elif "#" * 6 in left_half and "#" * 6 in right_half:
            symbol = "#"
            symbol_checker(symbol, left_half, right_half)

        elif "@" * 6 in left_half and "@" * 6 in right_half:
            symbol = "@"
            symbol_checker(symbol, left_half, right_half)

        elif "^" * 6 in left_half and "^" * 6 in right_half:
            symbol = "^"
            symbol_checker(symbol, left_half, right_half)

        else:
            print(f'ticket "{col}" - no match')

    else:
        print("invalid ticket")