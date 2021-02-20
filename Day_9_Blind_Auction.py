from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
store_information={}
def store(person_name,bid_information):
  store_information[bid_information]=person_name
run=True
max_bid=0
while run:
  print(logo)
  print("Welcome to secret auction program. ")
  name=input("What's you name ? \n")
  bid=int(input("What's you bid ?:\n$"))
  store(name,bid)
  if bid>max_bid:
    max_bid=bid
  more_bids=input("Are there any other bidders? Typre 'Yes' or 'No'?\n").lower()
  if more_bids=='no':
    run=False
    clear()
    print(f"The winner if {store_information[max_bid]} with a bid of ${max_bid} ")
  else:
    clear()

