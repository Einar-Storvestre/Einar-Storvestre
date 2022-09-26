innskudd = 10000

belop = 0

while belop < 200000:
    belop = innskudd
    for i in range(9):
        belop = belop * 1.021 + innskudd
        print(belop)
    innskudd += 1

print(innskudd)