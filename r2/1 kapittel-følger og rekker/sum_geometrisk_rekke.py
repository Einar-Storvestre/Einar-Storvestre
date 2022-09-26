# kode som bruker formelen for summen i en geometrisk rekke
a1 = 30
k = 2/5
n = 100

sum = a1*(k**n - 1)/(k - 1)  #formelen for summen i en geometrisk rekke

print(f"1: Med sumformel blir summen {sum}.")


#Kode som bruker en salgs sigma. går gjennom alle a_1 og plusser de sammen. bruker formelen for a_n

a1 = 1
k = -1/2
n = 1000

sum = 0

def f(x):
    return a1 * k**(x-1)  # a_n

for i in range(1, n + 1):
    sum += f(i)
    print(sum)
print(f"2: ved \"sigma\" kode ble summen {sum}.")



