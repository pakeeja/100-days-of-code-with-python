logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

from replit import clear
def add(a,b):
  return a+b
def substract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b
def power(a,b):
  return a**b
ans=0.0
take_input=True
num1=0
run=True
while run:
  if take_input:
    print(logo)
    num1=float(input("What's the first number? "))
  print("+\n-\n*\n/\n^\n")
  operation=input("Pick an operation ? ")
  num2=float(input("What's the next Number ? "))
  operations={
    '+':add,
    '-':substract,
    '*':multiply,
    '/':divide,
    '^':power,
  }
  ans=operations[operation](num1,num2)
  print(f"{num1} {operation} {num2} = {ans}")
  print(f"Type y to continue calculating with {ans}, or type 'n' to start a new calculation or else print any other key to EXIT!!? ")
  decision=input().lower()
  if decision =='n':
    ans=0.0
    clear()
  elif decision == 'y':
    print()
    take_input=False
    num1=ans
    ans=0.0
  else:
    run=False
    clear()
    print("Thank You!!")