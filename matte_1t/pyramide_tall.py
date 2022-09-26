p = 0
g = 0
etasjer = int(input("hvor mange etasjer?: "))
for i in range(etasjer):
    p += i + 1
    print(p)
    g += p

print(f"antall bokser som trengs er {g}")