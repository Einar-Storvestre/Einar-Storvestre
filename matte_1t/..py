

j = -3

laveste = 1000

def f(x):
    return -2*x**3-4*x**2+9*x-4


while j < 3:
    if f(j) < laveste:
        laveste =f(j)
    j += 0.001


print(f"bunnpunkt er {round(laveste,4)}, {round(f(laveste),4)}")