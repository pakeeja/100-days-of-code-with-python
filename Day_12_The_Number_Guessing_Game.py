logo="""

  ________                            .__                   ________                       
 /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 

"""
import random
from replit import clear
def guessing(number,attempts):
  while attempts>0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess=int(input("Make a Guess : "))
    if guess > number:
      print("Too High!")
      attempts-=1
      if not attempts==0:
        print("Guess Again.\n")
    elif guess < number:
      print("Too Low!")
      attempts-=1
      if not attempts==0:
        print("Guess Again.\n")
      
    else:
      print(f"You got it ! The answer was {number}")
      attempts=-1
  if attempts==0:
    print(f"\nYou've run out of guesses, You lose !!\nThe number was {number}")




game_not_over=True
while game_not_over:
  clear()
  print(logo)
  print("Welcome to The Number Guessing Game!!")
  print("I am thinking of a number between 1 and 100")
  number=random.randint(1,100)
  #print(number)
  print("You can make 10 attempts in EASY mode and 5 attempts in HARD mode.")
  level=input("Choose a difficulty ? Type 'easy' or 'hard'? ")
  if level=="easy":
    guessing(number,10)
  elif level=="hard":
    guessing(number,5)
  else:
    print("Wrong Iput!!")
  restart=input("\nDo you want to play the Game again? Type 'y' or 'n'? ")
  if not restart=='y':
    game_not_over=False
    clear()
    print("Thank you")

