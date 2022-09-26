import numpy as np
import matplotlib.pyplot as plt
#Laster inn fila og henter tidenefra første kolonne og posisjonene fra andre kolonne.
data = np.loadtxt("fjærvogn_copy.txt")
t = data[:,0]
s = data[:,1]

#Lager posisjonsgrafen.
plt.figure(1)
plt.plot(t,s)
plt.grid()
plt.title("Posisjon")
plt.xlabel("$t$ / s")
plt.ylabel("$s$ / m")
plt.show()


 #Teller n målinger og lager en liste for farten.
n = len(t)
v = np.zeros(n-1)

#Regner ut gjennomsnittsfarten for hvert tidspunkt ved å bruke posisjonen i punktet før og etter.
for i in range(1,n-1):
    v[i] = (s[i+1]-s[i-1])/ (t[i+1]-t[i-1])

#Lager fartsgrafen.
plt.figure(2)
plt.plot(t[1:n-1],v[1:n-1])
plt.grid()
plt.title("Fart")
plt.xlabel("$t$ / s")
plt.ylabel("$v$ / (m/s)")
plt.show()
#Lager en liste for akselerasjon.
a = np.zeros(n-2)

#Regner ut akselerasjonen for hvert tidspunkt ved å bruke farten i punktet før og etter.
for i in range(2,n-2):
    a[i] = (v[i+1]-v[i-1])/ (t[i+1]-t[i-1])

plt.figure(3)
plt.plot(t[2:n-2],a[2:n-2])
plt.grid()
plt.title("Akselerasjon")
plt.xlabel("$t$ / s")
plt.ylabel("$a$ / (m/s$^2$)")
plt.show()