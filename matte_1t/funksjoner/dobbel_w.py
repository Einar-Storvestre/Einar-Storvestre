import matplotlib.pyplot as plt

x = [0, 2, 4, 6, 8]
y = [4, 0, 2, 0, 4]


plt.scatter(x, y)
plt.plot(x, y)


# plotter
plt.xlabel("x-akse")
plt.ylabel("y-akse")


plt.legend()
plt.grid()
plt.show()