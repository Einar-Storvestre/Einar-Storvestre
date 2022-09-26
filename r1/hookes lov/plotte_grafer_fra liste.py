import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("fjærvogn.txt")
t = data[:, 0]
s = data[:, 1]

n = len(t)

#plotter posisjonsgraf
plt.figure(1)
plt.plot(t, s)
plt.grid()
plt.title("posisjon")
plt.xlabel("$t$ / s")
plt.ylabel("$s$ / m")

v = np.zeros(n - 1)

#plotter graf for momentan vekstfart ; (derivasjon) v=fart
for i in range(1, n - 1):
    v[i] = (s[i + 1] - s[i - 1]) / (t[i + 1] - t[i - 1])

plt.figure(2)
plt.plot(t[1:n - 1], v[1:n - 1])
plt.grid()
plt.title("Fart")
plt.xlabel("$t$ / s")
plt.ylabel("$v$ / (m/s)")

a = np.zeros(n - 2)

#plotter graf for momentan vekstfart; 2x(derivasjon) a=akselerasjon
for i in range(6, n - 6):
    a[i] = (v[i + 4] - v[i - 4]) / (t[i + 4] - t[i - 4])
    #print(round(a[i],2))  #lagt til
plt.figure(3)
plt.plot(t[2:n - 2], a[2:n - 2])
plt.grid()
plt.title("Akselerasjon")
plt.xlabel("$t$ / s")
plt.ylabel("$a$ / (m/s$^2$)")

plt.show()