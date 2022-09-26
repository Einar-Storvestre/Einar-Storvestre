import matplotlib.pyplot as plt
import numpy as np


def f(x):
    # ---Bytt med aktuell funksjon--
    return 340*0.82**x


def g(x):
    return (f(x + 0.0001) - f(x)) / 0.0001


def origo():
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')


# ----------------------------
# Bytt ut -10 og 10 med dine x-min og x-max
x = np.linspace(-5, 5, 1000)


# ----------------------------

def tegnGraf(x,y, navn):
    origo()
    plt.plot(x, y, label=navn)
    # -----------------------------------
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Et enkelt eksempel")
    plt.legend()
    plt.grid()
    plt.show()


y = f(x)
tegnGraf(x, y, "f")
y = g(x)
tegnGraf(x, y, "g")