from math import sqrt
from numpy import array
#Koordinater til hjørnene
ax, ay = -10, 0
bx, by = 2, 9
cx, cy = 14, -7

#Lagrer vektorer
OA = array([ax,ay])
OB = array([bx,by])
OC = array([cx,cy])

def lengde(v):
    return sqrt(v[0]**2 + v[1]**2)

# Regner ut sidelengder i trekanten
a = lengde(OC-OB)
b = lengde(OA-OC)
c = lengde(OB-OA)
# omkrets
s = a+b+c
# Radius og sentrum
S = (a*OA + b*OB + c*OC)/s
r = sqrt((s-2*a)*(s-2*b)*(s-2*c)/s)/2
print(f"Radius er {r}")
print(f"Sentrum er {S}")