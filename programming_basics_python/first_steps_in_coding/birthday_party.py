#разходи
#наем = входни данни
#цена на тортата = 20% от наема
#напитки – цената им е 45% по-малко от тази на тортата
#аниматор – цената му е 1/3 от цената за наема на залата


rent = float(input())
cacke = rent * 0.2
drinks = cacke - cacke * 0.45
animator = rent / 3
total_expenses = rent + cacke + drinks + animator
print(total_expenses)