import turtle
import random
colors = ["red","green","pink","orange","brown","chocolate","blue","black"]
for i in range(3,9):
    angle = 360/i
    turtle.pencolor(random.choice(colors))
    for _ in range(i):
        turtle.forward(100)
        turtle.right(angle)

turtle.exitonclick()