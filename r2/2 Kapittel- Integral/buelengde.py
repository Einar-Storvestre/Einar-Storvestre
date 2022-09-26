from math import sqrt
from math import log
from math import e


a= int(input("start-verdi: "))
b= float(input("slutt-verdi: "))

n = 10000 #antall punkter
Sum = 0

def f(x):
    return x*e**x


dx = (b-a)/n  # avstanden mellom hver måling


for i in range(a,n+1):
    avstand = sqrt( dx**2 +  (f(a+(i+1)*dx) - f(a+i*dx))**2)

    Sum += avstand

print(Sum)
