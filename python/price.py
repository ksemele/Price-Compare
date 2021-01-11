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
        self.price = float(price_units[0])
        self.units = float(price_units[1])
        if len(price_units) > 2:
            self.name = price_units[2:]

    def calc_price_per_unit(self):
        self.price_per_unit = self.price / self.units

    def __str__(self):
        return f"name: '{self.name}', " \
               f"price: {self.price}, " \
               f"units: {self.units}, " \
               f"price_per_unit: {self.price_per_unit}"


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
    print(f'\033[31mmin\033[00m item: {min_item}')
    print(f'\033[31mmax\033[00m item: {max_item}')
    #     diff = item_b.price_per_unit / (item_a.price_per_unit / 100) - 100  # todo make intelligent diff
    #     print(f"A less than B on {round(diff, 2)}%")


def barcode():  # todo testing working barcode scan
    from PIL import Image
    import zbarlight
    '''
    $ brew install zbar
    $ export LDFLAGS="-L$(brew --prefix zbar)/lib"
    $ export CFLAGS="-I$(brew --prefix zbar)/include"
    $ pip install zbarlight
    '''

    # file_path = './barcode.png'
    # file_path = './1.jpg'
    file_path = './2.jpg'
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()

    codes = zbarlight.scan_codes(['ean13'], image)
    print('QR codes: %s' % codes)


if __name__ == '__main__':
    # SQLite part -> to module?
    con = sqlite3.connect('goods.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS goods(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barcode INTEGER DEFAULT 0,
            name TEXT,
            units FLOAT DEFAULT 0
            );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS stores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            adress TEXT
            );""")
    con.commit()

    items = []
    print('input price mass [name] or empty line for finish input')
    while True:
        price_units = input("item price mass [name]: ")
        if len(price_units.split()) >= 2:
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
    if user_input.lower() == 'y':  # todo do save()
        # save()
        print('Ok, save. Which store is it?')
    if user_input.lower() == '2':  # todo test input to barcode scan
        barcode()
