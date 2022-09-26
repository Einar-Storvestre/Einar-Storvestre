import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return x**3+4*x-3

X = np.linspace(-3, 3, 200)
Y = f(X)

plt.plot(X, Y)
plt.grid()
plt.show()