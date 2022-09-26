import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Global_temp_GISS.txt")

t = data [:,0]
s = data[:,1]


#teller n målepunkter
n = len(t)

#lager posisjonsgrafen
plt.figure(1)
plt.title("Posisjonsgraf")
plt.xlabel("$t$ / s")
plt.ylabel("$s$ / m")
plt.grid()
plt.plot(t,s, "bx")  #plt.plot(t,s, "bx") :betyr kryss der punkter er målt ... plt.plot(t,s) gir glatt linje
plt.show()


#Lager fartsgrafen.
di = 1                                  # bestemmer hvor stor delta skal være. Det bestemmer hvor stor/liten tidsperiode
                                        # det regnes ut momentan fart på
v = np.zeros(n-di)
for i in range(di,n-di):
    v[i] = ((s[i+di]-s[i-di]) / (t[i+di]-t[i-di]))


plt.figure(2)
plt.title("Fartsgraf")
plt.xlabel("$t$ / s")
plt.ylabel("$v$ / (m/s)")
plt.grid()
plt.plot(t[di:n-di], v[di:n-di])
plt.show()

#Lager akselerasjonsgrafen.
dia = 1                              # bestemmer hvor stor delta skal være (hvor glatt kurven blir) hvor stor avstand det er mellom målingene.
di = di+dia
a = np.zeros(n-di)
for i in range(di,n-di):
    a[i] = ((v[i+dia]-v[i-dia]) / (t[i+dia]-t[i-dia]) )

plt.figure(3)
plt.title("Akselerasjonsgraf")
plt.xlabel("$t$ / s")
plt.ylabel("$a$ / (m/s$^2$)")
plt.grid()
#plt.ylim(-2,3)
plt.plot(t[di:n-di], a[di:n-di])
plt.show()



#Finner potensielleenergien i det ballen slippes
#m=0.450  #masse til objektet
#h= 1.80  # høyde det slippes fra
#g=9.81
#Formel for potensiellenergien er m*g*h
#Potensiell_energi = m*g*h
#print(f"Den potensielle energien før ballen slippes er {Potensiell_energi} Joule")#Finner høydetap ved å se på endringen i ballposisjonen ved å se på tallene jeg fikk fra trackeren, og der sto det at den var -0.537m fra starthøyde. Jeg henter ut tallet fra fila "skateR!.txt"
#htap = 0.537  #hentet ut fra skateR1
#h2 = h-htap # orginal høyde - høydetap. bruker samme formel for potensiellenergi, h2 -> gir høyden til andre svingning.
#print(f"Den nye potensielle energien til ballen når den har gått en gang frem og tilbake er {m*g*h2} Joule")#Finner energietapet
#print(f"Energitapet er {(m*g*h2)-(m*g*h)} Joule")#Vi avrunder verdiene for energitapet for å ha tre gjeldende sifre, fordi det er tre som er antallet
#Avrund_energitap=round((m*g*h2)-(m*g*h), 2)
#print(f"Energitapet overført til omgivelsene er {Avrund_energitap}Joule")

