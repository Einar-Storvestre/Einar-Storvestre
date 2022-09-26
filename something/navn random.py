import random

liste_tall = []

antall_nummer = 17

for i in range(antall_nummer):
    liste_tall.append(i)

print(liste_tall)

for i in liste_tall:
    B = random.choice(liste_tall)
    print(liste_tall[B])



