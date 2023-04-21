from money.money import Money
from abc import ABC, abstractmethod
from decimal import Decimal

entertainment_tax_rate = Decimal('0.07')
tax_rate = Decimal('0.0625')


class Candy:
    price_per_pound = Money('4.75','USD')

    def __init__(self, weight):
        self.weight = weight

    def calc_total(self):
        return round(Candy.price_per_pound * self.weight, 2)

    def calc_tax(self):
        return round(self.calc_total() * tax_rate, 2)


# cookie
class Cookie:
    Price_per_dozen = Money('6.25', 'USD')

    def __init__(self, dozen):
        self.dozen = dozen

    def calc_total(self):

        return round(Cookie.Price_per_dozen * self.dozen, 2)

    def calc_tax(self):
        return round(self.calc_total() * tax_rate, 2)


# cream
class IceCream:
    price_per_scoop = Money('1.70', 'USD')

    def __init__(self, scoops):
        self.scoops = scoops

    def calc_total(self):
        return round(IceCream.price_per_scoop * self.scoops, 2)

    def calc_tax(self):
        return round(self.calc_total() * tax_rate, 2)


# sundae

class Sundae:
    class HotFudge:
        cost = Money('1.25', 'USD')

    class Caramel:
        cost = Money('.50', 'USD')

    class StrawberrySyrup:
        cost = Money('.75', 'USD')

    class Peanuts:
        cost = Money('.35', 'USD')

    class Coconut:
        cost = Money(".20", 'USD')

    class AllToppings:
        cost = Money('3.05','USD')

    def __init__(self):
        self.toppings = []

    def add_toppings(self, topping):
        self.toppings.append(topping.cost)

    def calc_total(self):
        ice = IceCream(2)
        return sum(self.toppings) + ice.calc_total()

    def calc_tax(self):
        return round(self.calc_total() * tax_rate, 2)

    def tax_with_total(self):
        return self.calc_total() + self.calc_tax()
