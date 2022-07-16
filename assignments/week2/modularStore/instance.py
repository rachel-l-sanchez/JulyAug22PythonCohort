from store import Store
from store import Product

tienda = Store('Tienda')
shirt = Product('Floral blouse', "tops", 45.99)
blouse = Product('shirt', "tops", "69.00")
heels = Product('Black stilettos', "shoes", 75.99)
jeans = Product('Jeans', "pants", 69.99)
tienda.add_product(jeans)
tienda.add_product(heels)
tienda.add_product(shirt)
jeans.update_price(.25, True).print_info()
tienda.inflation(.10)
jeans.print_info()
# jeans.inflated()
shirt.set_clearance("tops", .15)
shirt.print_info()
jeans.sell_product(1)



























































