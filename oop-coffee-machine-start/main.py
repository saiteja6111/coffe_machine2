from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



coffemake1 = CoffeeMaker()
menu1 = Menu()
menuitem1 = MenuItem('latte',200,150,24,2.50)
menuitem2 = MenuItem('espresso',50,0,18,1.50)
menuitem3 = MenuItem('cappuccino',250,100,24,3.00)
Money1 = MoneyMachine()

while True:
    user_choice = input(f"Enter your choice {menu1.get_items()} : ")

    if user_choice.lower() == menuitem1.name:

        resource = coffemake1.is_resource_sufficient(menuitem1) 
        if resource == True:
            Money1.make_payment(menuitem1.cost)
            coffemake1.make_coffee(menuitem1)
        elif resource == False:
            break

    elif user_choice.lower() == menuitem2.name:

        resource = coffemake1.is_resource_sufficient(menuitem2)
        if resource == True:
            Money1.make_payment(menuitem2.cost)
            coffemake1.make_coffee(menuitem2)
        elif resource == False:
            break

    elif user_choice.lower() == menuitem3.name:

        resource = coffemake1.is_resource_sufficient(menuitem3) 
        if resource == True:
            Money1.make_payment(menuitem3.cost)
            coffemake1.make_coffee(menuitem3)
        elif resource == False:
            break

    elif user_choice.lower() == 'report':

        coffemake1.report()
        Money1.report()





