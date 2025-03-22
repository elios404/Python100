from logo import image
import os

def calculate(first, operator, second):
    if operator == "+":
        result = first+second
    elif operator == '-':
        result = first-second
    elif operator == '*':
        result = first*second
    elif operator == '/':
        result = first/second
    else:
        print("wrong operator!!")
        result = 0
    print(f"{first_num} {operator} {second_num} = {result}")
    return result


def check_keep(result):
    check = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if check == 'y':
        return True
    else:
        return False

end = False

while not end:
    print(image)
    
    first_num = float(input("What's the first number? : "))
    operator = input("Choose ur operator between + , - , * , /  :  " )
    second_num = float(input("What's the second number? : "))
    
    result = calculate(first_num, operator, second_num)

    keep = check_keep(result)
    
    while keep:
        operator = input("Choose ur operator between + , - , * , /  :  " )
        second_num = float(input("What's the second number? : "))
        result = calculate(result,operator,second_num)
        keep = check_keep(result)

    os.system('clear')