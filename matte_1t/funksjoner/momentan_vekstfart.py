def f(x):  # funskjonen
    return 0.001 * x ** 3 - 0.09 * x ** 2 + 2.4 * x + 74


def g(x):  # momentan vekstfart
    return (f(x + 0.00001) - f(x)) / 0.00001


# vekstfarten når x=5??

X = 0
while X < 51:
    if g(X) < 0.5:
        if g(X)>0.49:
            print(X)
    X += 0.01



