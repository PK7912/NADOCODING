# import Basic_8_4_7_module_theater_module
# Basic_8_4_7_module_theater_module.price(3)  # 3명이서 영화 보러 갔을 때 가격
# Basic_8_4_7_module_theater_module.price_morning(4)  # 4명이서 조조 할인 영화 보러 갔을 때
# Basic_8_4_7_module_theater_module.price_soldier(5)  # 5명이서 군인 할인 영화 보러 갔을 때

# import Basic_8_4_7_module_theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from Basic_8_4_7_module_theater_module import *
# # == from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from Basic_8_4_7_module_theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5) #error

from Basic_8_4_7_module_theater_module import price_soldier as price
price(5)
