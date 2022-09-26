#n gjester
n = int(input("hvor mange gjester?: "))
trykk_antall = 0
n = n-1

for i in range(n):
    trykk_denne_runden = n-i
    trykk_antall += trykk_denne_runden
    print(trykk_denne_runden)


print( trykk_antall )
