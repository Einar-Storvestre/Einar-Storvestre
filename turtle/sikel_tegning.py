import turtle
p = 0
turtle.speed(70)
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()

#dette gjør at loopen kjører 10 ganger

for count in range(int(30)):
    r = p + 0
    p = r + 10
    turtle.circle(p)
    r = p + 10

turtle.mainloop()