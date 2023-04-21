from MenuItem import *


class Order:
    def __init__(self, item, ammount):
        self.item = item
        self.ammount = ammount

    def sweet(self):
        what_you_want = self.item(self.ammount)
        return what_you_want.calc_total()

    def tax(self):
        what_you_want = self.item(self.ammount)
        return what_you_want.calc_tax()

    def total_with_tax(self):
        what_you_want = self.item(self.ammount)
        return what_you_want.calc_total() + what_you_want.calc_tax()
