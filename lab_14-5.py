# Author: ATN 3/21/22

import turtle

# defining the movement of the turtle
def move_forward():
    t.forward(50)


def move_backward():
    t.backward(50)


def turn_left():
    t.left(90)


def turn_right():
    t.right(90)


# setting the screen size
window = turtle.Screen()

# naming the turtle and giving its color and speed
t = turtle.Turtle()
t.fillcolor("violet")
t.speed(0)

# register events

window.onkey(move_forward, "Up")
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")
window.listen()


window.mainloop()
