#이 코드는 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#에서 미로 문제를 해결하기 위한 코드를 작성한 것이다.
#일부 함수는 웹에서 구현된 것이기에 실제로 이 코드를 동작했을 때 작동하지 않는다.
def move():
    return 0
def turn_left():
    return 0
def wall_in_front():
    return 0
def wall_on_right():
    return 0
def front_is_clear():
    return 0
def right_is_clear():
    return 0
def at_goal():
    return 0

#--- 이 이후부터 웹에 적용하면 된다. ---

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# 문제가 생기는 상황은 주변에 아무런 벽이 없는 상황일 때이다.
def no_wall_around():
    if wall_in_front() or wall_on_right():
        return False
    else:
        turn_left()
        turn_left()
        if wall_in_front() or wall_on_right():
            turn_left()
            turn_left() #다시 원래 상태로 복귀
            return False
        else:
            turn_left()
            turn_left()
            return True
        
while not at_goal():
    if no_wall_around():
        while front_is_clear() and right_is_clear():
            move()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

#--- 더 간단한 방법이 있었다 ---
# 우리는 오른벽을 따라 가는 법칙을 찾는데 처음 출발하는 위치가 오른 벽이 존재하지 않는 경우 문제가 생길 수 있다.
# 그렇다면 작성한 알고리즘을 실행하기 전에 시작하는 위치를 오른쪽 벽이 있게 하도록 하면 되지 않는가?

# while not at_goal() 전에

while front_is_clear():
    move()
turn_left()
#를 하면 무조건 오른쪽 벽이 있는 상태로 시작할 수 있다.