# Author: ATN 3/18/22

import turtle

# setting the screen size
window = turtle.Screen()
window.setup(500, 500)
window.screensize(450, 450)

# setting the background color and naming the window
turtle.Screen().bgcolor("gray")
window.title("Lab 3")

# naming the turtle and giving its shape and pen color
t = turtle.Turtle()
t.shape("turtle")
t.pencolor("violet")

# looping its movements evenly
for x in range(3):
    t.right(180)
    t.forward(200)
    t.left(60)

window.mainloop()
