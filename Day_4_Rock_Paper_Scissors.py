import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image=[rock,paper,scissors]
choice=int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors.\n"))
game=[0,1,2]
print(image[choice])
computer_choice=random.randint(0,2)
print("Computer chose: \n")
print(image[computer_choice])
if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 
elif choice==0 and computer_choice==2 or choice==2 and computer_choice==1 or choice==1 and computer_choice==0:
  print("YOU WIN!!")
elif choice==2 and computer_choice==0 or choice==1 and computer_choice==2 or choice==0 and computer_choice==1:
  print("YOU LOSE!!")
else:
  print("It's a DRAW!!")