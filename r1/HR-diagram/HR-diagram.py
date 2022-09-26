

#navnet til stjernen er i kolonne 0.
#overflatetemperatur er i kolonne 1.
#utstrålt effekt er ik kolonne 2.

#oppgaven: bruk dataene og lag et HR-diagram.

import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("stjernedata.txt", usecols=(1,2), delimiter=",")
T = data[:,0]
P = data[:,1]

plt.figure(1)
plt.yscale("log")
plt.axis([max(T),min(T),min(P),max(P)])
plt.xlabel("overflatetemperatur i kelvin")
plt.ylabel("utstrålt effekt / $P_\odot$")



plt.grid()


#plt.scatter(T,P,".")
plt.legend("Einar er veldig kul")  ##
plt.title("Einar er en fet type")   ###
plt.suptitle("HR-diagram")
plt.get_plot_commands()

plt.plot(T,P,".")
plt.show()