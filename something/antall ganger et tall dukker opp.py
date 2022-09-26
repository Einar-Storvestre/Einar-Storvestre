


# telle n tall
#f.eks ved
# forloop går gjennom alle tall og sjekker om det er det du vil telle hvis det er en variabel øker
teller = 0
first = int(input("Fra hvilket tall begynner intervallet?: "))
last = int(input("Hvilket tall slutter intervallet med?: "))
tall = int(input("hvilket tall?: "))
for i in range(first,last+1):
    set1 = set(str(i))
    if f"{tall}" in set1:
         teller+=1

print(teller)

