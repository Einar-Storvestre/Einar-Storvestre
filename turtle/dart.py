import turtle
import random

# bakgrunn
wn = turtle.Screen()
wn.title("EINARS SUPER KULE SPILL SOM BARE HANDLER OM FLAKS")
wn.bgcolor("grey")
wn.setup(width=1000, height=1000)



turtle.speed(100)

x_akse = 0
# denne som skal endres
y_akse = 0

turtle.pencolor('white')

turtle.penup()
turtle.goto(x_akse, y_akse)
turtle.pendown()

diameter = 7
forflyttning = 20

hvor_stor = input("vil du ha anbefalt størrelse på dartskiven?: ")
if hvor_stor == "ja":
    hvor_stor = 8

if hvor_stor == "nei":
    hvor_stor = input("hvor stor vil du ha da?: ")
hvor_mage_piler = input("hvor mange piler vil du kaste?: ")

for count in range(int(hvor_stor)):
    turtle.circle(diameter)
    turtle.penup()
    y_akse = y_akse - 40
    turtle.goto(x_akse, y_akse)
    diameter = diameter + 40
    turtle.pendown()

turtle.penup()

for count in range(int(hvor_mage_piler)):
    def x():
        return random.randint(-250, 250)


    def y():
        return random.randint(-250, 250)


    turtle.goto(x(), y())
    turtle.pendown()

    farge = random.choice('rgy')

    if farge == 'r':
        turtle.pencolor('red')
        turtle.fillcolor('red')
        turtle.begin_fill()

    if farge == 'g':
        turtle.pencolor('green')
        turtle.fillcolor('green')
        turtle.begin_fill()

    if farge == 'y':
        turtle.pencolor('yellow')
        turtle.fillcolor('yellow')
        turtle.begin_fill()

    turtle.circle(5)
    turtle.penup()
    turtle.end_fill()



turtle.mainloop()
