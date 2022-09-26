from numpy import array
x_A = float(input("x-koordinaten til A: "))
y_A = float(input("y-koordinaten til A: "))

x_B = float(input("x-koordinaten til B: "))
y_B = float(input("y-koordinaten til B: "))
x_D = float(input("x-koordinaten til D: "))
y_D = float(input("y-koordinaten til D: "))

#origo A vektor
OA = array([x_A, y_A])

#BC vektor

AD = array([x_D - x_A, y_D - y_A])

AB = array([x_B - x_A, y_B-y_A])
#AD vektor = BC vektor

DC=AB
#origo-A vektor + AD vektor er OD vektor.
OC=OA+AD+AB

print("D har koordinatene (", OC[0], ",", OC[1], ")")