import time
import random
visuelle = []
mulige_ord_liste = ['bil', 'einar','bil', 'katt', 'einar', 'penger',
                    'kattepus', 'hund', 'andorra', 'norge', 'lysestake', 'vinkel_i_grader', 'mamma', 'ahtene', 'fykles vei', 'tre', 'brannmann']
for i in range(8):
    visuelle.append(random.choice(mulige_ord_liste))

print(visuelle)
print(f"hva kan du egentlig huske? her kommer 8 ting prøv å memmoriser: ")
print(visuelle)
time.sleep(1)
print("\n"*100)

antall = 0
tilfeldig_plass_nummer = random.randint(0, len(visuelle)-1)
tilfeldig_plass_huske_ord = visuelle[tilfeldig_plass_nummer]


gjettning = input(f"hvilket ord var på plassen {tilfeldig_plass_nummer+1}: ")
if gjettning == visuelle[tilfeldig_plass_nummer]:
    print("bra du er flink")
else:
    print("nei nei")

print(f"hei det er utvikleren her... har du lyst til å legge til en ting som andre burde huske? ")
legge_til_liste = input("ja/nei: ")
if legge_til_liste == "ja":
    while True:
        antall +=1
        tillagt_liste = input("hva vil du legge til?: ")
        mulige_ord_liste.append(tillagt_liste)

        if antall % 3 == 0:
            stopper = input("vil du stoppe?: ")
            if stopper == "ja":
                break
else:
    print("neivel. det går fint...")

print(mulige_ord_liste)

