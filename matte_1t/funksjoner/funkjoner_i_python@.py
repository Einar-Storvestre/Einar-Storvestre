import matplotlib.pyplot as plt
import numpy as np

# lager en funksjon som setter opp aksene i origo
def origo():
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')


#hoved_tekst = x**4 + 2*x**3 - 37* x **2 + 10*x + 168
# definerer funksjonen f
def f(x):
    hoved = x**4 + 2*x**3 - 37* x **2 + 10*x + 168
    return hoved

# legger inn x-verdier
x = np.linspace(10,10, 1000)      #hva er definisjonsmengden? hva er de mulige utverdiene??

# beregner y-verdier
y = f(x)

# setter opp aksene
origo()


#plotter
plt.plot(x,y,label = f"f(x)= x**4 + 2*x**3 - 37* x **2 + 10*x + 168")  #label=str(y))
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.title("einar er kul")
plt.legend()
plt.grid()
plt.show()