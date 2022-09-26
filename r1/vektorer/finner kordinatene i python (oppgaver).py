from numpy import array
x_A = float(input("x-koordinaten til A: "))
y_A = float(input("y-koordinaten til A: "))

x_B = float(input("x-koordinaten til B: "))
y_B = float(input("y-koordinaten til B: "))
x_C = float(input("x-koordinaten til C: "))
y_C = float(input("y-koordinaten til C: "))

#origo A vektor
OA = array([x_A, y_A])
#BC vektor
BC = array([x_C - x_B, y_C - y_B])

AB = array([x_B - x_A, y_B-y_A])
#AD vektor = BC vektor
AD=BC
DC=AB
#origo-A vektor + AD vektor er OD vektor.
OD=OA+AD

print("D har koordinatene (", OD[0], ",", OD[1], ")")