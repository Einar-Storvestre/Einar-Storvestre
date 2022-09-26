def f(x):
    return x**2-3
laveste_verdi = 100

for i in range(-10,10):
    if f(i) < laveste_verdi:
        laveste_verdi = f(i)

print(laveste_verdi)