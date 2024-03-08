import turtle

turtle.color('green','pink') # pencolor, second fillcolor
turtle.begin_fill()
for _ in range(9):

    turtle.forward(200)
    turtle.left(120)


#turtle.rt(90)
turtle.penup()
turtle.goto(100,-200)


turtle.pendown()
turtle.hideturtle()
turtle.pensize(10)
turtle.circle(100)

print(turtle.pos())
turtle.shape("turtle")



turtle.end_fill()

#turtle.pencolor('red')
#turtle.fillcolor('red')

turtle.exitonclick()