from logo import logo
import os

def dock_string(text):
    '''
    this is a example of dock string
    '''
    return 0

exp = dock_string("hello")

print(logo)
print("Welcome to the secret auction program.")
game_over = False
record = {}


while not game_over:
    name = input("What's ur name?:  ")
    bid = int(input("What's ur bid?:  $"))
    record[name] = bid
    
    check_game_over = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
    if check_game_over == 'yes':
        os.system('clear')
    if check_game_over == 'no':
        game_over = True

highest_bid = 0
who_gets = ''
for name, bid in record.items():
    if bid > highest_bid:
        who_gets = name
        highest_bid = bid
print(f"The winner is {who_gets} with a bid of ${highest_bid}")