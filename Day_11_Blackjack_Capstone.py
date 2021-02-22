############### Blackjack Project #####################
import random
from replit import clear
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
           

def deal_card():
  cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J']
  return random.choice(cards)


def calculate_score(list):
  score=0
  nl=[]
  for i in list:
    if i=='K' or i=='Q' or i=='J':
      score+=10;
    elif i=='A':
      nl.append(i)
    else:
      score+=i
  for i in nl:
    if score>10:
      score+=1
    else:
      score+=11
  return score


def compare(user_score,computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def draw_cards():
  list=[deal_card(),deal_card()]
  return list


def game():
  print(logo)
  user_cards= draw_cards()
  computer_cards= draw_cards()
  game_over=False

  while not game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}\n")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      print()
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        game_over = True
    
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}\n")
  print(compare(user_score, computer_score))
  print() 


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  clear()
  game()
clear()
print("THANK YOU !! 🙃")


