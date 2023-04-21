import sys
from MenuItem import *

from Order import *
import os

no = "no"
def what():
    item_list = [Candy, Cookie, IceCream, Sundae]
    end_list = []
    while True:

        i = int(input("\rwhat would you like to order.\n 1-candy\n 2-cookie\n 3- ice cream\n 4-sundae\n 5- done\n "
                         "give number\n"))
        if i == 1 or i == 2 or i == 3 or i == 4:
            get_order(item_list[i - 1], i, end_list)

        elif i == 5:
            print(end_list)
            break

        else:

            print('please input an integer between 1 and 5')


def get_order(item, num_value, item_list):
    unit_of_measure = ["pounds", "dozen", 'scoops']
    items = ["candy", "cookie", "ice cream", "sundae"]
    if num_value == 1 or num_value == 2 or num_value == 3:
        ammount = int(input(f"how many {unit_of_measure[num_value - 1]} of {items[num_value - 1]} would you like"))
        i = Order(item, ammount)
        item_list.append((items[num_value-1], i.sweet(), i.tax, i.total_with_tax()))

    elif num_value == 4:
        sun = Sundae()
        toppings_list = [Sundae.HotFudge, Sundae.Caramel, Sundae.StrawberrySyrup, Sundae.Peanuts, Sundae.Coconut, Sundae.AllToppings]
        while True:
            topping = int(input("what would you want atop the sundae.\n 1- hot fudge\n 2- caramel\n 3- strawberry "
                                "syrup\n 4- peanuts\n 5- cococut\n 6- all topings\n 7- done\n"))
            if topping < 7:
                sun.add_toppings(toppings_list[topping - 1])

            elif topping == 7:
                item_list.append(("sundae", str(sun.calc_total()), str(sun.calc_tax()), sun.tax_with_total()))
                break

            else:
                print("invalid entry. do number between 1 and 7")
    else:
        print("this should not be possible")


def main():
    print("welcome to the candy shop.")
    what()


main()
