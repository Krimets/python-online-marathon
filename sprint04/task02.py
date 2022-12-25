class Pizza:
    num = 0
    def __init__(self, ingredients):
        Pizza.num += 1
        self.order_number = Pizza.num
        self.ingredients = ingredients
        self.pizza_type = ", ".join(ingredients)

    @staticmethod
    def garden_feast():
        return Pizza(["spinach", "olives", "mushroom"])

    @staticmethod
    def hawaiian():
        return Pizza(["ham", "pineapple"])

    @staticmethod
    def meat_festival():
        return Pizza(["beef", "meatball", "bacon"])




p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
p2 = Pizza.garden_feast()                  # order 2
print(p1.ingredients)  #["bacon", "parmesan", "ham"]
print(p2.ingredients)  #["spinach", "olives", "mushroom"]
print(p1.order_number) # ➞ 1
print(p2.order_number) # ➞ 2