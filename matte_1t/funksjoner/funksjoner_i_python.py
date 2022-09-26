import matplotlib.pyplot as plt
# legger inn x-verdier og y-verdier
x = [0,2,4,6,8]
y = [4,0,2,0,4]

# plotter verdiene
plt.plot(x,y,'g')

# tekst
plt.title("Dobbel-v")
plt.legend()
plt.grid()
# viser plottet
plt.show()

