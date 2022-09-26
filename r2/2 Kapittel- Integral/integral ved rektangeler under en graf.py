n = int(input("Antall rektangel: "))

a = int(input("startverdi: "))   #startverdi
b = int(input("Sluttverdi: "))   #sluttverdi

dx = (b - a) / n  #bredden på hvert rektangel

def f(x):
    return x**2

sum = 0

for i in range(a, n+1):  #regner ut summen av arealene til rektanglene.
    xi = a + (i - 1) * dx  #    formelen for en n i en aritmeisk rekke
    sum += f(xi)*dx

print(sum)


