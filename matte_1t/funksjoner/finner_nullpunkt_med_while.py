def f(x):
    return 2*x**2-1

start = -2
slutt = 2.5

while start < slutt:
    if round(abs(f(start)),4)<0.001:
        print(f"dette er et nullpunkt {round(start,4)}")
    start +=0.0001
