# from window import Window
# window = Window(400, 300,)  # "PriceCompare v0.2")
# window.run()

good_a = input("input price, mass A: ")
good_a = good_a.split()
price_a = float(good_a[0])
mass_a = float(good_a[1])
good_b = input("input price, mass B: ")
good_b = good_b.split()
price_b = float(good_b[0])
mass_b = float(good_b[1])

price_per_a = price_a / mass_a
price_per_b = price_b / mass_b

if price_per_a < price_per_b:
	diff = price_per_b / (price_per_a / 100) - 100
	print(f"A less than B on {round(diff, 2)}%")
if price_per_b < price_per_a:
	diff = price_per_a / (price_per_b / 100) - 100
	print(f"B less than A on {round(diff, 2)}%")

user_input = input('Save result? Y(es) / N(o): ')
# if user_input == 'Y':  # todo do save()
# 	save()