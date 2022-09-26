import numpy as np
a= float(5   )
b= float(8   )
c= float(11.3   )

s = (a+b+c)/2

herons_formel = np.sqrt(s*(s-a)*(s-b)*(s-c))

print(herons_formel)