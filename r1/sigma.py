#sigma
sum = 0

start_tall = 0
slutt_tall = 100

teller = start_tall

for teller in range(slutt_tall +1 ):
    sum += teller
    print(teller)


print(f"sigma balls {sum} ")