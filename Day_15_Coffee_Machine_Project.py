# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def report(d):
    print(f"Water : {d['water']}ml")
    print(f"Milk : {d['milk']}ml")
    print(f"Coffee : {d['coffee']}g")
    print(f"Money : ${d['money']}\n\n")

dict={
    'water':300,
    'milk':200,
    'coffee':100,
    'money':0,
}
def insert(price):
    a=float(input("How many quarters? "))
    b=float(input("How many dimes? "))
    c=float(input("How many nickles? "))
    d=float(input("How many pennies? "))
    money_given=0.25*a+0.10*b+0.05*c+0.01*d;
    if money_given>=price:
        price=money_given-price
        return price
    else:
        return -1.0




def expresso():
    if dict['water']>=50 :
        if dict['coffee']>=18:
            print("Please insert coins")
            left=insert(1.50)
            if left==-1.0:
                print("\nSorry that's not enough money")
                return False
            else:
                if left> 0.0:
                    print(f"Here is ${round(left,2)} dollars in change")
                print("Here is your espresso ☕. Enjoy!\n")
                return True

        else:
            print("\nSorry there is not enough Coffee")
            return False
    else:
        print("\nSorry there is not enough Water")
        return False


def latte_cappucino(choice,water,milk,coffee,price):
    if water<=dict['water']:
        if milk<=dict['milk']:
            if coffee<=dict['coffee']:
                print("Please insert coins")
                left=insert(price)
                if left==-1.0:
                    print("\nSorry that's not enough money")
                    return False
                else:
                    if left> 0.0:
                        print(f"Here is ${round(left,2)} dollars in change")
                    print(f"Here is your {choice} ☕.  Enjoy!\n")
                    return True
            else:
                print("\nSorry there is not enough Coffee")
                return False
        else:
            print("\nSorry there is not enough Milk")
            return False
    else:
        print("\nSorry there is not enough Water")
        return False








order=True
while order:
    user_input=input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input=='report':
        report(dict)
    elif user_input=='espresso':
        if expresso():
            dict['water']-=50
            dict['coffee']-=18
            dict['money']+=1.50
        else:
            order=False
    elif user_input=='latte':
        water=200
        coffee=24
        milk=150
        price=2.50
        if latte_cappucino(user_input,water,milk,coffee,price):
            dict['water']-=200
            dict['coffee']-=24
            dict['milk']-=150
            dict['money']+=2.50
        else:
            order=False

    elif user_input=='cappuccino':
        water=250
        coffee=24
        milk=100
        price=3.00
        if latte_cappucino(user_input,water,milk,coffee,price):
            dict['water']-=250
            dict['coffee']-=24
            dict['milk']-=100
            dict['money']+=3.00
        else:
            order=False

    else:
        print("Wrong Choice")
        order=False


