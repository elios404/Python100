#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#random.choice(list_name) 을 통해서 리스트 안에서 랜덤하게 요소를 뽑을 수 있다.--> 더 간단한 작성법

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ""
for i in range(nr_letters):
    random_letter = random.randint(0,25) #엄밀히 보면 잘못 된 구현, 대문자를 포함하지 않음
    easy_password += letters[random_letter]
for i in range(nr_symbols):
    random_symbols = random.randint(0,8)
    easy_password += symbols[random_symbols]
for i in range(nr_numbers):
    random_number = random.randint(0,9)
    easy_password += numbers[random_number]

print(easy_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = ""
char_num = [nr_letters, nr_numbers, nr_symbols]
total_length = sum(char_num)
for i in range(total_length):
    which_character = random.randint(0,2)
    while char_num[which_character] == 0:
        which_character = random.randint(0,2)
    char_num[which_character] -= 1
    if which_character == 0:
        hard_password += random.choice(letters)
    elif which_character == 1:
        hard_password += random.choice(numbers)
    elif which_character == 2:
        hard_password += random.choice(symbols)

print(hard_password)

#---------------------------- 더 간단한 버전
password_list = []

for i in range(nr_letters):
    password_list += random.choice(letters)
for i in range(nr_symbols):
    password_list += random.choice(symbols)
for i in range(nr_numbers):
    password_list += random.choice(numbers)
print(password_list)
#이 부분이 간단하게 만듬
random.shuffle(password_list)
print(password_list)
# 문자 리스트를 문자열로 만드는 방법, 각 요소들을 ""를 사이에 두고 join한다.
password = ''.join(password_list)

print(f"Your password is {password}")