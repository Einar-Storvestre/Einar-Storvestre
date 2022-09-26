s= 0 #m
t= 0 #s
dt= 0.01 #s
v= 10 #m/s
m= 2000 #kg
g = 9.81 #m/s^2

def my(s):
    return 0.7 #0.2 + 0.1*s**0.2

def R(s):
    return my(s)*m*g

while v > 0:
    a = -R(s)/m
    v = v + a*dt
    s = s + v*dt

print("Bremselengden er",round(s,2))