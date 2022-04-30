from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    order = input(f"What would you like?({menu.get_items()}): ").lower()
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        is_on = False
    else:
        item = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)