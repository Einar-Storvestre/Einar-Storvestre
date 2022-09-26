import matplotlib.pyplot as plt
# legger inn x-verdier og y-verdier
x = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [2,4,6,8,10]

# plotter verdiene
plt.scatter(x,y1, label = "graf 1")
plt.scatter(x,y2, label = "graf 1")
plt.plot(x,y1,y2)
# tekst
plt.xlabel("x-verdier")
plt.ylabel("y-verdier")
plt.title("Et enkelt eksempel")
plt.legend()
plt.grid()
# viser plottet
plt.show()