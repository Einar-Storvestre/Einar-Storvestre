def f(x):
    return x**2+5*x-2

for i in range(-10, 10):
    if f(i) < 0:  # hvis f(i) er negativ (siste negative verdi)
        n = i
    elif f(i) > 0:  # hvis f(i)er positiv
        p = i
    else:
        print(f"f av {i} er {f(i)}")

# midpunkt er m = (a+b)/2

for i in range(40):
    m = (n + p) / 2
    if f(m) > 0:  # hvis m er positvt
        p = m
    if f(m) < 0:  # hvis m er negativt
        n = m

print(f"her er nullpunktet {m}")