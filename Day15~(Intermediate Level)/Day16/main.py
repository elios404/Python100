#about OOP 객체지향 프로그래밍에 대해서 

import turtle
from turtle import Turtle, Screen

# import module
# print(module.valuable)

t1 = turtle.Turtle()
#turtle.py 와 같은 파일에서 Trutle() 클래스를 t에 선언함.

t2 = Turtle()
#Turtle을 따로 import 했기에 바로 사용
t2.shape("turtle")
t2.color("red")
t2.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()