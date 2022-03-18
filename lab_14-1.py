# Author: ATN 3/17/22

import turtle

# setting the screen size
window = turtle.Screen()
window.setup(1000, 1000)
window.screensize(950, 950)

# naming the turtle
t = turtle.Turtle()

# controlling the movements
t.right(90)
t.forward(250)
t.left(90)
t.forward(100)
t.left(90)
t.forward(250)
t.left(90)
t.forward(100)

window.mainloop()
