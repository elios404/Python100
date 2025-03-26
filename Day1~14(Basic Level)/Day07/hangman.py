#직접 만들어본 행맨 게임

import image
import random

print(image.intro)

answer_words = ['apple', 'orange', 'pear', 'hangman', 'python', 'lemon' , 'bread' , 'banana']
word = random.choice(answer_words)
lives = 6
included_char = []
to_compare = '_'*len(word)

while lives > 0:
    print("Word to guess:", end = ' ')
    print(to_compare)
    
    guess = input("Guess a letter: ").lower()

    if guess in word:
        included_char.append(guess)
        to_compare = ''
        for char in word:
            if char in included_char:
                to_compare += char
            else:
                to_compare += "_"
        print(to_compare)
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    
    if to_compare == word:
        print(f"***********************IT WAS {word}! YOU WIN**********************")
        break

    
    print(image.lives_image[lives])
    if lives > 0:
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    else:
        print(f"***********************IT WAS {word}! YOU LOSE**********************")