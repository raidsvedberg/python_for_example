import turtle

for i in range(1, 4):
    for r in range(1, 5):
        turtle.begin_fill()
        turtle.color('black', 'blue')
        turtle.forward(100)
        turtle.right(90)
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()
turtle.exitonclick()