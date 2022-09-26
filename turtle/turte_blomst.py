import turtle

t = turtle.Pen()

turtle.speed(1000)

turtle.bgcolor('black')

colors = ['red', 'purple', 'blue', 'green', 'orange']

for i in range(360):
    t.pencolor(colors[i % 5])
    t.width(i//100+1)
    t.forward(i)
    t.left(59)

turtle.mainloop()




