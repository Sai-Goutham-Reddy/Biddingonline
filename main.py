from clear import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to Biding!!!!!")
bid = {}
heighest_person = ""
heighest_amount = 0
bid_not_finished = True
while bid_not_finished:
  name = input("What is your name? ")
  amount = int(input("What is your bid amount $"))
  bid[name] = amount
  finish = input("Are there are any other Biders say 'yes' or 'no'.\n").lower()
  if finish == "no":
    bid_not_finished = False
  clear()
for person in bid:
  if bid[person] > heighest_amount:
    heighest_amount = bid[person]
    heighest_person = person
print(f"The winner is {heighest_person} with a bid of ${heighest_amount}")