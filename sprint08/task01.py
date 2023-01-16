import unittest



class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def __init__(self, *products_list):
        self.products_list = products_list

    @staticmethod
    def discount(product_count):
        if product_count > 20:
            return 0.5
        elif product_count >= 20:
            return 0.7
        elif product_count >= 10:
            return 0.8
        elif product_count >= 7:
            return 0.9
        elif product_count >= 5:
            return 0.95
        else:
            return 1

    def get_total_price(self):
        return sum([product.price * product.count * self.discount(product.count) for product in self.products_list[0]])

class CartTest(unittest.TestCase):
    def test_discount(self):
        expected = 0.95
        actual = Cart().discount(5)
        self.assertEqual(actual, expected)


products = (Product('p1', 10, 4),
            Product('p2', 100, 5),
            Product('p3', 200, 6),
            Product('p4', 300, 7),
            Product('p5', 400, 9),
            Product('p6', 500, 10),
            Product('p7', 1000, 20))
cart = Cart(products)
print(cart.get_total_price())