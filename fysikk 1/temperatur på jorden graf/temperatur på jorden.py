
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Global_temp_GISS.txt")

tid = data[:,0]

temperatur = data[:,1]


plt.figure()
plt.plot(tid, temperatur)

plt.show()

