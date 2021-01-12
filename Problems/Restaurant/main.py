import itertools

dishes = itertools.product(main_courses, desserts, drinks)

prices = itertools.product(price_main_courses, price_desserts, price_drinks)

all_items = zip(dishes, prices)


