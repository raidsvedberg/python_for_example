import turtle
import random

turtle.pensize(3)

for r in range(0, 8):
    turtle.color(random.choice(["red", "blue", "black", "yellow", "green", "purple"]))
    turtle.forward(50)
    turtle.right(45)

turtle.exitonclick()
