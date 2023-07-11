# TurtleDrawMax.py
import turtle
t = turtle.Pen()
t.speed(0)
turtle.onscreenclick(t.setpos)
turtle.bgcolor("blue")
t.pencolor("green")
t.width(99)

# This allows the window to stay up.
turtle.done()
