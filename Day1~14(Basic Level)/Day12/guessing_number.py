from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

difficulty = input('Choose the difficulty. Type "easy" or "hard" : ').lower()
lives = 0
if difficulty == 'easy':
    lives = 10
elif difficulty == "hard":
    lives = 5

answer = random.randint(1,100)

while lives > 0:
    print(f"You have {lives} remaining to guess the number.")
    user_guess = int(input("Make ur guess between 1~100 : "))
    
    if user_guess == answer:
        print(f"Correct! The answer is {answer}!!")
        break
    elif user_guess > answer:
        print(f"Too high!!")
    else:
        print(f"Too low..")
    
    lives -= 1
    if lives == 0:
        print(f"You lose all your lives!! The answer is {answer}")
    else:
        print("Guess again \o/")
    print()