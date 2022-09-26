from math import sqrt
a = 0.8
b = 39.2
c = -33.6*2

x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-sqrt(b**2-4*a*c))/(2*a)

print("Løsningene er x =", x1, "og x =", x2)