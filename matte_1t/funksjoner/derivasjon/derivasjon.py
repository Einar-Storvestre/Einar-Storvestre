def f(x):
    return 100000*1.015**x

onsket_okning = 2000



for i in range(100):
    differanse= f(i)-f(i-1)
    if differanse>onsket_okning:
        print(i)
        break


def f(x):  # funskjonen
    return 0.001 * x ** 3 - 0.09 * x ** 2 + 2.4 * x + 74


def g(x):  # momentan vekstfart
    return (f(x + 0.00001) - f(x)) / 0.00001


# vekstfarten når x=5??

X = 0
while X < 51:
    if g(X) < 5:
        if g(X) > 4.9:
            print(X)
    X += 0.1
