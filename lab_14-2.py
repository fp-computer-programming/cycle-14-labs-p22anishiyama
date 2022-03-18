# Author: ATN 3/17/22

import turtle

# setting the screen size
window = turtle.Screen()
window.setup(500, 500)
window.screensize(450, 450)

# naming the turtle
t = turtle.Turtle()

# controlling the movements
t.right(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

window.mainloop()
