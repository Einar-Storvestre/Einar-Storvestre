import time
print("du får se dette i femten sekunder")
#from kem_e_best_ import tegning
#tegning1=tegning
#tegning1.funksjon(self)
#hvor lange de kan se teksten
sekunder=3
#så lager jeg en for loop som teller ned
for nedtelling in range(sekunder):
    print(str(sekunder-nedtelling)+ " gjennværende sekunder")
    #hvor mange sekunder den er mellom hvert sekund
    time.sleep(1)

print("\n"*200)

poeng=0

def correct(poeng1):
    poeng1= poeng1 + 1
    print(str(poeng1) + " av 3")
    print("bra jobbet")
    return poeng1


def feil(poeng):
    print("bedre lykke neste gang")
    print(str(poeng) + " av 3")
    return poeng


svar1=input("hvilken farge var huset? ")


if svar1=="gult":
    poeng = correct(poeng)


else:
    feil(poeng)


svar2=input("hva het han i det gule huset? ")

if svar2=="fredrik":
    poeng=correct(poeng)
else:
    feil(poeng)
print(str(poeng) + " av 3")