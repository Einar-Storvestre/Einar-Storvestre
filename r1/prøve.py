from math import log


def f(x):
    return log(x)


def derivert(a):
    return ((f(a + 0.000001) - f(a)) / 0.000001)

for i in range(1,11):
    a = i
    print(f"{derivert(a)} er den deriverte av f der a = {a}")