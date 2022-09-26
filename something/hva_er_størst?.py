def storste (a,b,c):
    if a < b and b > c:
        print(b)
    elif a> b and a>c:
        print(a)
    elif c>a and c>b:
        print(c)

print(storste(1,6,3))