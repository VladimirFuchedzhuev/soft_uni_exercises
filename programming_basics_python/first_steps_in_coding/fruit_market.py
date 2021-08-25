#Вход
#От конзолата се четат 5 реда:
#Цена на ягодите в лева – реално число;
#Количество на бананите в килограми – реално число;
#Количество на портокалите в килограми – реално число;
#Количество на малините в килограми – реално число;
#Количество на ягодите в килограми – реално число.

#цената на  малините е на половина по-ниска от тази на ягодите;
#цената на портокалите е с 40% по-ниска от цената на малините;
#цената на бананите е с 80% по-ниска от цената на малините.
#входни данни
strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberry_kg = float(input())
#цени на продукти
raspberries_price = strawberry_price / 2
oranges_price = raspberries_price - raspberries_price * 0.4
bananas_price = raspberries_price - raspberries_price * 0.8
#разход за продукти
total_strawberry = strawberry_kg * strawberry_price
total_raspberries = raspberries_price * raspberries_kg
total_bananas = bananas_kg * bananas_price
total_oranges = oranges_kg * oranges_price
#общо разходи
total_sum = total_strawberry + total_raspberries + total_bananas + total_oranges

print(total_sum)