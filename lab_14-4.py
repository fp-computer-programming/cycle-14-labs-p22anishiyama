# Author: ATN 3/18/22

import turtle

# setting the screen size
window = turtle.Screen()

# naming the window
window.title("Lab 4")

# naming the turtle and giving its color and speed
t = turtle.Turtle()
t.fillcolor("violet")
t.speed(0)

# control the movements of the turtle
t.stamp()
t.goto(100, 100)
t.fillcolor("light green")
t.begin_fill()
for x in range (4):
    t.forward(100)
    t.right(90)
t.end_fill()

window.mainloop()
