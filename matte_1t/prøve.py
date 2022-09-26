def f(x):
    return x**3-2*x+1

p= -100

while f(p) <0:
    p+=0.001
print(p,  f(p))

for i in range(-10,10):
    if f(i)==0:
        print(i)