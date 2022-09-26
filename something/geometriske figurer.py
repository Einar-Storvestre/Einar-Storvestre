import turtle

wn = turtle.Screen()
bird = turtle.Turtle()
bird.speed(13)
bird.pensize(4)
bird.color("black")
bird.setpos(0, 0)
bird.fillcolor("pink")

#trekant
bird.forward(150)
bird.left(120)
bird.forward(150)
bird.left(120)
bird.forward(150)

#forflyttning
bird.penup()
bird.forward(150)
bird.pendown()


#firkant
bird.forward(150)
bird.left(90)
bird.forward(150)
bird.left(90)
bird.forward(150)
bird.left(90)
bird.forward(150)
















wn.exitonclick()





