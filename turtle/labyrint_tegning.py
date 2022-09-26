import turtle

p = 500

turtle.speed(30)
for count in range(int(60)):
    turtle.forward(p)
    turtle.left(90)
    p = p * 0.9
turtle.mainloop()


###

#import turtle

#p = 0

#turtle.speed(30)
#for count in range(int(40)):
  #  p = p + 10
  #  turtle.forward(p)
  #  turtle.left(90)

#turtle.mainloop()
