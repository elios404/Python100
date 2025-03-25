from art import logo
import os
import random

def check():
    b = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ").lower()
    if b == 'y':
        return True
    elif b == 'n':
        print("Good Bye My Friend")
        return False
    else:
        print("Wrong input!! Choose ur option again!")
        check()

def draw_card(player, computer):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player.append(random.choice(cards))
    computer.append(random.choice(cards))

def check_gameover(player):
    if sum(player) > 21:
        change = False
        if 11 in player:
            player.remove(11)
            player.append(1)
            change = True
        if change:
            check_gameover(player)
        else:
            return True
    else:
        False

def asking_draw_card():
    check = input("Type 'y' to get another card, type 'n' to pass:").lower()
    if check == 'y':
        return True
    elif check == 'n':
        return False
    else:
        print("Make the input correctly!")
        asking_draw_card()

def showing_status(player, computer):
    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer's first card: {computer[0]}")

def check_result(player, computer, Black_jack = False):
    player_score = sum(player)
    computer_score = sum(computer)
    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer cards: {computer}, current score: {sum(computer)}")
    print(f"your score : {sum(player)} and comptuer score : {sum(computer)}")
    if Black_jack:
        print("Black Jack! You win!")
    elif player_score > computer_score or computer_score > 21:
        print("you win")
    elif player_score < computer_score:
        print("you lose")
    elif player_score == computer_score:
        print("Draw")

game_start = check()

while game_start:
    print(logo)
    my_cards = []
    com_cards = []
    for _ in range(2):
        draw_card(my_cards, com_cards)
    showing_status(my_cards, com_cards)  

    if sum(my_cards) >= 21:
        check_result(my_cards,com_cards, True)
        game_start = check()
        continue
    
    keep_drawing = asking_draw_card()
    is_over = False

    while keep_drawing:
        draw_card(my_cards, com_cards)
        is_over = check_gameover(my_cards)
        showing_status(my_cards, com_cards)
        if is_over:
            keep_drawing = False
        else:
            keep_drawing = asking_draw_card()
    
    if not is_over:
        check_result(my_cards, com_cards)
    else:
        print("your care over 21! you lose")
    game_start = check()
    os.system('clear')