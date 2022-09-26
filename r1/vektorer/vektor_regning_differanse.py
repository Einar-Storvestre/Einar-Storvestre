from numpy import array
x_u = float(input("x-koordinaten til u: "))
y_u = float(input("y-koordinaten til u: "))

x_v = float(input("x-koordinaten til v: "))
y_v = float(input("y-koordinaten til v: "))

u = array([x_u, y_u])
v = array([x_v, y_v])

print("u+v=",u+v)
print("u-v=",u-v)
print("2v + 3u =", 2*v + 3*u)