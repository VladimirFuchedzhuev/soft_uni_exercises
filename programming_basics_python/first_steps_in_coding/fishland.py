#bonito_price = mackerel_price + mackerel_price * 0.6
#horse_mackerel = spart_price + spart_price * 0.8
#mussels = 7.5lv
#
#
#
#
mackerel_price = float(input())
spart_price = float(input())
bonito_weight = float(input())
horse_mackerel_weight = float(input())
mussels_weight = int(input())


bonito_total = (mackerel_price + mackerel_price * 0.6) * bonito_weight
horse_mackerel_total = (spart_price + spart_price * 0.8) * horse_mackerel_weight
mussels_weight_total = mussels_weight * 7.5

total_expenses = bonito_total + horse_mackerel_total + mussels_weight_total

print(f"{total_expenses:.2f}")