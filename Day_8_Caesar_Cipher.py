logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
from replit import clear
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(txt,shft,cipher_direction):
  cipher_text=""
  if cipher_direction=="decode":
      shft*=-1
  for char in txt:
    if char in alphabet:
      required_index=alphabet.index(char)+shft
      if cipher_direction=="encode":
        if required_index<len(alphabet):
          cipher_text+=alphabet[required_index]
        else:
          cipher_text+=alphabet[required_index-len(alphabet)]
      else:
        cipher_text+=alphabet[required_index]
    else:
      cipher_text+=char
  print(f"\nThe {cipher_direction}d text is {cipher_text}\n")

print(logo)
run=True
while run:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction=='encode' or direction=='decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%len(alphabet)
    caesar(text,shift,direction)
  else:
    print("Wrong decision")

  
  decision=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if decision =='no':
    run=False
    clear()
    print("GOOD BYE ! \nCOME BACK AGAIN!!")
  else:
    clear()
    print(art.logo)

