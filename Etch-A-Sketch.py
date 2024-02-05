# PROJECT ON SKETCHING APP

from turtle import *

tommy = Turtle()
myscreen = Screen()

tommy.shape("classic")
tommy.pensize(3)

def move_forward():
    tommy.forward(10)

def move_backward():
    tommy.backward(10)

def move_clockwise():
    tommy.right(10)

def move_counterclockwise():
    tommy.left(10)

def clear_screen():
    tommy.home()
    tommy.clear()

myscreen.listen()

myscreen.onkey(move_forward, "Up")
myscreen.onkey(move_backward, "Down")
myscreen.onkey(move_clockwise, "Right")
myscreen.onkey(move_counterclockwise, "Left")
myscreen.onkey(clear_screen, "space")


myscreen.exitonclick()

