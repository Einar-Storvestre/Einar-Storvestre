from math import log


def f(x):
    return log(x)


a = int(input("verdi for a: "))


def derivert(a):
    return ((f(a + 0.000001) - f(a)) / 0.000001)


print(f"{derivert(a)} er den deriverte av f der a = {a}")