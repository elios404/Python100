# 계산기 연산자를 구분하는 새로운 방식, if문을 사용하지 않음

def add(n1, n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiple(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiple,
    '/' : divide,
}

#입력된 연산자 문자를 이용해 키를 기반으로 함수에 접근할 수 있다. 딕셔너리에 함수를 담는 새로운 방식
#사용할 떈
print(operations['+'](10,5))

#어떤 연산자를 사용할 수 있는지 보여줄땐
for symbol in operations:
    print(f"{symbol} ", end=" ")
print()
#이를 통해서 연산자와 함수를 추가할 때 함수만 작성하고 딕셔너리에 추가하기만 하면 된다.