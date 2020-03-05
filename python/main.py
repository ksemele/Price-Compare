from window import Window
window = Window(400, 300,)  # "PriceCompare v0.2")
window.run()

price_a = float(input("input price A: "))
mass_a = float(input("input mass A: "))
price_b = float(input("input price B: "))
mass_b = float(input("input mass B: "))
price_per_a = price_a / mass_a
price_per_b = price_b / mass_b
print(str(price_per_a), str(price_per_b))

