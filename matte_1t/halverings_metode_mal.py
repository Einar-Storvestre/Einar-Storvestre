#Bytt ut her med din funksjon
def f(x):
    return x**3-4*x**2
  #----------------------------

#Bytt ut 1 og 2 med det x-området du leter etter nullpunkt
#---------------------------------------------------------
a = 0
b = -6
#---------------------------------------------------------

for i in range(100):
  m = (a+b)/2
  if f(a)*f(m)<0:
    b = m
  else:
    a = m

print(f"Løsning: x = {(a+b)/2:0.3f}")  # 10 iterasjoner gir 3 korrekte desimaler.
