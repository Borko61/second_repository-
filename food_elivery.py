chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())
price_chicken_menu = chicken_menu * 10.35
price_fish_menu = fish_menu * 12.40
price_veg_menu = veg_menu * 8.15
whole_menu_price = price_chicken_menu + price_fish_menu + price_veg_menu
price_dessert = whole_menu_price * 0.20
price_delivery = 2.50
amount_order = whole_menu_price + price_dessert + price_delivery
print(amount_order)