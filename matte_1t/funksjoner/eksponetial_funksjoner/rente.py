
x=0

rente = (1+    -8     /100)
print(rente)

innsats = 3254

def renter(x):
    return innsats*rente**x


while renter(x)> 1000:
    x +=1



print(x)
print(renter(x))


