from math import sqrt
from numpy import array

a = float(input("Tast inn a: "))
b = float(input("Tast inn b: "))
r = float(input("Tast inn r: "))
s = float(input("Tast inn s: "))
t = float(input("Tast inn t: "))


#Lagrer vektor fra midten av sirkelen til punktet p(s,t)
f = array([(s-a),(t-b)])


def lengde(v):
    return sqrt(v[0]**2 + v[1]**2)

if lengde(f)==r:
    print("punktet ligger på sirkelen")

if lengde(f)<r:
    print("punktet ligger innenfor sirkelen")

if lengde(f)>r:
    print("punktet ligger utenfor sirkelen")

