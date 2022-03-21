# Author: ATN 3/21/22

import turtle

# setting the screen size
window = turtle.Screen()

# naming the turtle and giving its color and speed
t = turtle.Turtle()
color = window.textinput("Color", "Please choose a turtle color: ")
t.color(color)
t.shapesize(window.numinput("Size", "Please choose a turtle size (1-5): "))

# creating the function for drawing a square
def draw_square():
    t.fillcolor(color)
    t.begin_fill()
    for x in range(4):
        t.right(90)
        t.forward(100)
    t.end_fill()


# checking for user click
window.onclick(draw_square(), btn=1)

window.mainloop()
