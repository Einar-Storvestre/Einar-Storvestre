def f(x):
    return (2*x-6)/(x+1)

    #if x < 2:
     #   return (7/10)*x
    #else:
     #   return x**(1/2)

svar = input("Velg verdi for a:")
a = float(svar)
t = 1.0

while t > 0.00001:
    print("f(" + str(round(a - t, 7)) + ") = ", round(f(a - t), 7))
    t = t/10

t = 1.0
while t > 0.00001:
    print("f(" + str(round(a + t, 7)) + ") = ", round(f(a + t), 7))
    t = t/10