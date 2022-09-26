import matplotlib.pyplot as plt
import numpy as np

# definerer funksjonen f
def f(x):
    return x**2+5*x - 10

# legger inn x-verdier
x = np.linspace(-10,10, 1000)

# beregner y-verdier
y = f(x)

# plotter
plt.plot(x,y, label = r'$f(x)=x^2$')       #hva du vil etter =
plt.xlabel("x")
plt.ylabel("y")
plt.title("Et enkelt eksempel")
plt.legend()
plt.grid()
plt.show()