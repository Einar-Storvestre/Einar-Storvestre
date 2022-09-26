

def T(x):
    return 0.00144 * x ** 1.07       #meter gir minutter



p =0

while T(p) < 60:
    p+=0.1

print(p)

