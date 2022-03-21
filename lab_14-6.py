# Author: ATN 3/21/22

import turtle

# setting the screen size
window = turtle.Screen()

# naming the turtle and giving its color and speed
t = turtle.Turtle()
t.color(window.textinput("Color", "Please choose a turtle color: "))
t.shapesize(window.numinput("Size", "Please choose a turtle size (1-5): "))

# creating the function for drawing a square
def draw_square():
    for x in range(4):
        t.right(90)
        t.forward(100)

# checking for user click
window.onclick(draw_square(), btn=1)

window.mainloop()
