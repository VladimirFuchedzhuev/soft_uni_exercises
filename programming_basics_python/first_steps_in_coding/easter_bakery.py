flour_price = float(input())
flour_weight = float(input())
sugar_weight = float(input())
eggs_boxes = int(input())
bread_yeast = int(input())

sugar_price = flour_price * 0.75
eggs_boxes_price = flour_price * 1.1
bread_yeast_price = sugar_price * 0.2

total_amount = flour_price * flour_weight + sugar_price * sugar_weight + eggs_boxes_price * eggs_boxes\
               + bread_yeast_price * bread_yeast
print(f"{total_amount:.2f}")

