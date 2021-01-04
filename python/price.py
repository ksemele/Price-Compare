# from window import Window
# window = Window(400, 300,)  # "PriceCompare v0.2")
# window.run()
import sqlite3


class Item:
    name = ''
    price = 0.0
    units = 0.0
    price_per_unit = 0.0

    def fill(self, price_units):
        price_units = price_units.split()
        if len(price_units) == 2:
            self.price = float(price_units[0])
            self.units = float(price_units[1])

    def calc_price_per_unit(self):
        self.price_per_unit = self.price / self.units

    def __str__(self):
        return f"name: '{self.name}', price: {self.price}, units: {self.units}, price_per_unit: {self.price_per_unit}"


def compare_price_per_unit(items):
    min_price = (min(x.price_per_unit for x in items))
    max_price = (max(x.price_per_unit for x in items))
    print(min_price, max_price)
    min_item = None
    max_item = None
    for each in items:
        if each.price_per_unit == min_price:
            min_item = each
        elif each.price_per_unit == max_price:
            max_item = each
    print('min item:', min_item)
    print('max item:', max_item)
    #     diff = item_b.price_per_unit / (item_a.price_per_unit / 100) - 100  # todo make intelligent diff
    #     print(f"A less than B on {round(diff, 2)}%")


if __name__ == '__main__':
    con = sqlite3.connect('goods.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS goods(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT,
           units FLOAT DEFAULT 0
           );""")
    con.commit()

    items = []
    while True:
        price_units = input("input price, mass or empty line for finish input: ")
        if len(price_units.split()) == 2:
            item = Item()
            item.fill(price_units)
            try:
                item.calc_price_per_unit()
                items.append(item)
            except ZeroDivisionError:
                print("Wrong price. Can't be a zero")
        elif price_units == '':
            print('\nOkay, this is some goods:')
            break

    for each in items:
        print(each)

    compare_price_per_unit(items)
    user_input = input('Save result? Y(es) / N(o): ')
    if user_input == 'Y':  # todo do save()
        # save()
        print('Ok, save. Wich store is it?')
