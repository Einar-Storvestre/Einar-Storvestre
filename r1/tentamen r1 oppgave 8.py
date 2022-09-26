import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (1 / 2) * x ** 2 - x + 3


xx = np.linspace(-10, 10, 200)

yy = f(xx)

plt.plot(xx, yy)  # plotter funksjonen f(x)
plt.plot(yy, xx)  # Plotter den omvendte funksjonen til f(x), ved å bruke y verdi som input og x verdi som output.
plt.axhline(y=0)
plt.axvline(x=0)
plt.grid()

