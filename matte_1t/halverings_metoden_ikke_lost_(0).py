def f(x):
    return x ** 2-2

def nullpunkt(a, b):
    for i in range(100):
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

    print(f"Løsning: x = {(a + b) / 2:0.3f}")  # 10 iterasjoner gir 3 korrekte desimaler.

b = 20

for a in range(-20,20):
    if a>-0.1:
        continue
    b = b - 1
    nullpunkt(a, b)

