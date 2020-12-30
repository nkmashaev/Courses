class Order:
    def __init__(self, price, discount_func):
        self.__price = price
        self.discount = discount_func

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Error: price expected to be positive")
        self.__price = value

    def del_price(self, value):
        del self.__price

    price = property(get_price, set_price, del_price, "order price")

    def final_price(self):
        return self.price - self.__price * self.discount(self)


def morning_discount(order):
    return 0.5


def flex_discount(order):
    if order.price > 100:
        return 0.25
    else:
        return 0.5
