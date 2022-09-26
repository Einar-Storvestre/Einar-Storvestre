mytuple = tuple(["max",28,"boston"])
mytuple1 = tuple(['p','f','a','b','j','s','d','e'])   #lager forkjellige tulpler som jeg kan hente ting ut av
print(type(mytuple))

item = mytuple[2]

print(item)
print("-----------")
color_codes = ((1,2,3),(4,6,5),(7,8,9))
print(color_codes)
print(color_codes.count(2))

if "max" in mytuple:
    print("yes max har komt")    #er ordet: max i mytuple?

if "p" in mytuple1:
    print("ja det er en p der")


a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5]    #fra 2 til 5
c = a[::-1]  #baklengs

print(c)
print(b)


#why tuples is more space efficent then lists
import sys
list1 = [0,1,2,"hei", True]
tuple1 = (0,1,2,"hei", True)
print(sys.getsizeof(list1), "bytes er i listen")   # hvor stor er plassforkjellden
print(sys.getsizeof(tuple1), "bytes er i tupelen")


import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))  # ser her at tuples bruker kortere tid og tar mindre plass
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))

temperatur = [221, 223, 245, 233, 226, 788, 762, 245]

nye_temperaturer = []

for temperatur in temperatur:
    nye_temperaturer.append(temperatur / 10)
print(nye_temperaturer)