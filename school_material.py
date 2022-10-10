import math
number_pack_of_pens = int(input())
cost_pack_of_pen = 5.80 * number_pack_of_pens
number_pack_of_markers = int(input())
cost_pack_of_markers = 7.20 * number_pack_of_markers
litres_detergent = int(input())
cost_litres_detergent = 1.20 * litres_detergent
percent_discount = int(input())
percent_discount = percent_discount / 100
full_amount = (cost_pack_of_pen + cost_pack_of_markers + cost_litres_detergent)
discount_amount = full_amount -(full_amount * percent_discount)
print(discount_amount)






 #print(amount)
