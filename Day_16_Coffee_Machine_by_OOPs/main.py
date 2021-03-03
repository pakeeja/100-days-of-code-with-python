from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee=CoffeeMaker()
money=MoneyMachine()

order=True
while order:
  
  user_input=input(f"What would you like:? ({menu.get_items()}): ")
  if user_input=="off":
    order=False
  elif user_input=="report":
    coffee.report()
    money.report()
  else:
    drink=menu.find_drink(user_input)
    if drink!=None:
      is_enough_ingre=coffee.is_resource_sufficient(drink)
      is_payment=money.make_payment(drink.cost)
      if is_enough_ingre and is_payment:
        coffee.make_coffee(drink)







