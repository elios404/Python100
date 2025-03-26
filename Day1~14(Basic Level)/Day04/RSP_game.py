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

#하면서 느낀점 : if 문을 되는데로 사용하지 말고, 최대한 줄일 수 있는 방향으로 논리적으로 구성할 수 있도록 하자
#단순하게 if문으로 모든 것을 해결하려고 하지 말고 다른 방법이 없는지 생각해보자-->여기서는 아스키코드를 리스트에 담아서 리스트 인덱스로 if 문 없이 출력할 수 있다.

import random

game_image = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
me = int(input())
if me < 3 and me >= 0:
    print(game_image[me])

com = random.randrange(0,3)
print(f"Computer chose: {com}")
print(game_image[com])

if me >= 3 or me < 0:
    print("You choose the wrong number")
elif me == 0 and com == 2:
    print("You win!")
elif me == 2 and com == 0:
    print("You lose")
elif me == com:
    print("Draw!")
elif me > com:
    print("You win!")
else:
    print("You lose..")