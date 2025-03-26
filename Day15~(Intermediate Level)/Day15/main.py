global coffee_type

def print_resource(res):
    '''현재 있는 자원과 돈을 출력해주는 함수'''
    water = res["Water"]
    milk = res["Milk"]
    coffee = res["Coffee"]
    money = res["Money"]
    print(f"Water : {water}ml")
    print(f"Milk : {milk}ml")
    print(f"Coffee : {coffee}g")
    print(f"Money : ${money}")

def is_lack_resources(res, coffee):
    '''사용자가 원하는 음료를 만들기에 충분한 자원이 있는지 확인하는 함수, 부족하면 true를 반환'''
    # global coffee_type
    needed_resources = coffee_type[coffee]
    
    if resources["Water"] < needed_resources["Water"]:
        print("Sorry! There is not enough water.")
        return True
    
    if resources["Milk"] < needed_resources["Milk"]:
        print("Sorry! There is not enough Milk.")
        return True
    
    if resources["Coffee"] < needed_resources["Coffee"]:
        print("Sorry! There is not enough Coffee.")
        return True

    return False

def insert_coin():
    '''코인 갯수를 입력 받고 총 얼마를 투입했는지 계산하는 함수, 총 투입 금액을 반환'''
    print("Insert Coins, type how many coins you gonna insert with number.")
    how_many_quarters = int(input("How many quarters : "))
    how_many_dimes = int(input("How many dimes : "))
    how_many_nickles = int(input("How many nickles : "))
    how_many_pennies = int(input("How many pennies : "))
    money_userInsert = how_many_quarters*coin_value["quarters"] + how_many_dimes*coin_value["dimes"] \
        + how_many_nickles*coin_value["nickles"] + how_many_pennies*coin_value["pennies"]
    return money_userInsert

def is_enough_money(coffee, money):
    '''투입된 돈이 충분한지 확인하는 함수, 충분하면 true를 반환'''
    # global coffee_type
    if coffee_type[coffee]["Money"] < money:
        return True
    else:
        return False

def make_coffee(res, coffee, money):
    '''자원을 사용하여 커피를 만드는 함수, 사용된 자원만큼 자원이 줄고, 가격 만큼 돈이 올라간다. 바뀐 자원을 반환'''
    res["Water"] -= coffee_type[coffee]["Water"]
    res["Milk"] -= coffee_type[coffee]["Milk"]
    res["Coffee"] -= coffee_type[coffee]["Coffee"]
    res["Money"] += coffee_type[coffee]["Money"]
    change = money - coffee_type[coffee]["Money"]
    print(f"Here is your {coffee}! Your change is ${change:.2f}")
    
    return res

resources = {
    "Water" : 300,
    "Milk" : 200,
    "Coffee" : 100,
    "Money" : 0,
}
coffee_type = {
    "espresso" : {
        "Water" : 50,
        "Milk" : 0,
        "Coffee" : 18,
        "Money" : 1.5,
    },
    "latte" : {
        "Water" : 200,
        "Milk" : 150,
        "Coffee" : 24,
        "Money" : 2.5,
    },
    "cappuccino" : {
        "Water" : 250,
        "Milk" : 100,
        "Coffee" : 24,
        "Money" : 3.0,
    }
}
coin_value = {
    "quarters" : 0.25,
    "dimes" : 0.1,
    "nickles" : 0.05,
    "pennies" : 0.01,
}
machine_power = True

valid_input = ['espresso', 'latte', 'cappuccino', 'report', 'off']
while machine_power:
    # 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    input_word = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if input_word not in valid_input:
        print("Wrong input! Try again!")
        continue

    # 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if input_word == "off":
        machine_power = False
        continue

    # 3. Print report.
    if input_word == 'report':
        print_resource(resources)
        continue

    # 4. Check resources sufficient? if not back to No.1
    if is_lack_resources(resources, input_word):
        continue

    # 5. Process coins.
    money_userInsert = insert_coin()

    # 6. Check transaction successful?
    if not is_enough_money(input_word, money_userInsert):
        print("Sorry that's not enough money. Money refunded.")
        continue

    # 7. Make Coffee.
    resources = make_coffee(resources,input_word,money_userInsert)

