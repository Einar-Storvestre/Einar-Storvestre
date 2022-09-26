from math import sqrt

v0 = float(input("Skriv inn startfart i m/s: "))
v = float(input("Skriv inn sluttfart i m/s: "))
aks = float(input("Skriv inn akselerasjon i m/s^2: "))
s0 = float(input("Skriv inn starthøyde i m: "))

s = (v**2 - v0**2)/(2*aks) + s0
a = 0.5*aks
b = v0
c = s-s0

if (b**2-4*a*c) > 0:
    t1 = (-b - sqrt(b**2-4*a*c))/(2*a)
    t2 = (-b + sqrt(b**2-4*a*c))/(2*a)
    print("Gjenstanden når høyden", s, "m etter", t1, "s og etter", t2, "s.")

elif (b**2-4*a*c) == 0:
    t = -b/(2*a)
    print("Gjenstanden når høyden",s, "m og etter", t, "s.")

else:
    print("Ingen løsning.")