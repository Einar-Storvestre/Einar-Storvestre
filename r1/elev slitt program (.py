def f(x):
    return x/(x**2)

x= -3
dx= 0.01

while x<5:
    v1= f(x-dx)
    v2= f(x)
    v3= f(x+dx)
    if v1 < v2 and v2 > v3:
        print("toppunkt for x=", round(x,2))
    x+=dx

bunnpunkt_y = 100
bunnpunkt_x = 0

for i in range(-10,10):
    if f(i) < bunnpunkt_y:
        bunnpunkt_y = f(i)
        bunnpunkt_x = i

print(f" bunnpunkt til f(x) er ved ({bunnpunkt_x},{bunnpunkt_y})")
