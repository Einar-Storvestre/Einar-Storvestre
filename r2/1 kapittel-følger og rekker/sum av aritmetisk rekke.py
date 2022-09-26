
antall_ledd = int(input("Antall a_1? "))

sum = 0

for n in range(1, antall_ledd + 1):
    sum += 2*n

print(f"Summen av {antall_ledd} a_1 er {sum}.")