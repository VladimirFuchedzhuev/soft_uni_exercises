#вход
#Дължина в см – цяло число
#Широчина в см – цяло число
#Височина в см – цяло число
#Процент зает обем – реално число
#действия
#обем на аквариум = дължина * ширина * височина в см кубини
#обем в литрли = обем на аквариум / 1000
#заета част =
lenght = int(input())
width = int(input())
hight = int(input())
occupied_volume = float(input())

aquarium_volume = lenght * width * hight
aquarium_liters = aquarium_volume / 1000
occupied_volume_percent = occupied_volume / 100
needed_liters = aquarium_liters * (1 - occupied_volume_percent)
print(needed_liters)

