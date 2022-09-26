#n = input("hvilken figur?: ")
#n = int(n)
#Areal = (n + 2) ** 2
#gra = (n+2) + (n+2) + n + n
#print(int(gra))
#print(Areal)
antall_morke = 0
samlet_verdi = 0

for n in range(1, 101):
    antall_morke = (n+2)**2-n**2
    samlet_verdi += antall_morke
    print(f"figur nr {n} har {antall_morke} mørke ruter")

print(samlet_verdi)

