masse = [15.2, 14.9, 14.8, 15.0, 15.3, 15.2, 14.9, 15.1]
sum_masse = 0
antall = 0
maks_masse = masse[0]
min_masse = masse[0]

for m in masse:
    print(m)
    sum_masse = sum_masse + m
    antall = antall + 1
    if m > maks_masse:
        maks_masse = m
    if m < min_masse:
        min_masse = m

gjsnitt_masse = sum_masse/antall
avvik = (maks_masse - min_masse)/2

print("Det perfekte jordbær veier",
        round(gjsnitt_masse,1), "±",
        round(avvik,1))