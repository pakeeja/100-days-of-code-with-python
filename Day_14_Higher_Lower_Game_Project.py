from art import logo
from art import vs
from game_data import data
from replit import clear
import random


current_score=0
correct=True
while correct:
  clear()
  print(logo)
  if not current_score==0:
    print(f"You're right! Current score: {current_score}")
  player1=random.choice(data)
  player2=random.choice(data)
  while player1['name']==player2['name']:
    player2=random.choice(data)
  print(f"Compare A: {player1['name']}, a {player1['description']}, from {player1['country']}")
  print(vs)
  print(f"Against B: {player2['name']}, a {player2['description']}, from {player2['country']}")
  decision=input("Who has more followers? Type 'A' or 'B': ").lower()
  if decision=='a':
    if player1['follower_count']>player2['follower_count']:
      current_score+=1
    else:
      clear()
      print(f"Sorry,that's wrong.Final score:{current_score}")
      correct=False
  else:
    if player1['follower_count']<player2['follower_count']:
      current_score+=1
    else:
      clear()
      print(f"Sorry,that's wrong.Final score:{current_score}")
      correct=False


  


