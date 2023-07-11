# ColorSquareSpiral.py
import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)

# This allows the window to stay up.
turtle.done()
