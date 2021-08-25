easter_bread = int(input())
eggs = int(input())
cookies = int(input())
eggs_paint = 0.15

easter_bread_price = 3.2 * easter_bread
eggs_price = 4.35 * eggs
cookies_price = 5.4 * cookies
eggs_paint_price = 12 * eggs * eggs_paint

total_expenses = easter_bread_price + eggs_price + cookies_price +eggs_paint_price

print(f"{total_expenses:.2f}")
