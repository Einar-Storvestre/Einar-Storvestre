import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("skateR1.txt")
t = data[:, 0]
s = data[:, 1]

n = len(t)

plt.figure(1)
plt.plot(t, s)
plt.grid()
plt.title("posisjon")
plt.xlabel("$t$ / s")
plt.ylabel("$s$ / m")


dx_v = 3 #delta x for veolocity (glatting for v (fart). høyere verdi gir en mer glatt graf.
v = np.zeros(n - dx_v)

#Regner ut momentan fart  (derivasjon) v=fart
for i in range(dx_v, n - dx_v):
    v[i] = (s[i + dx_v] - s[i - dx_v]) / (t[i + dx_v] - t[i - dx_v])

plt.figure(2)
plt.plot(t[dx_v:n - dx_v], v[dx_v:n - dx_v])
plt.grid()
plt.title("Fart")
plt.xlabel("$t$ / s")
plt.ylabel("$v$ / (m/s)")


dx_a = 5 #delta x for akselerasjon (glatting for akselerasjon. høyere verdi gir en mer glatt graf
a = np.zeros(n - dx_v)

#regner ut akselerasjon  (derivasjon) a=akselerasjon

for i in range(dx_a, n - dx_a):
    a[i] = (v[i + dx_a] - v[i - dx_a]) / (t[i + dx_a] - t[i - dx_a])
    #print(round(a[i],2))  #lagt til

plt.figure(3)
plt.plot(t[dx_a:n - dx_a], a[dx_a:n - dx_a])
plt.grid()
plt.title("Akselerasjon")
plt.xlabel("$t$ / s")
plt.ylabel("$a$ / (m/s$^2$)")

plt.show()
