p= 0
onsket = int(input("hva vil du ha?: "))
onske_oppfylt = False

while p<20:
    p+=1
    y = p
    summen = y
    for i in range(p):

        summen *= (y-i)-1
        #print(f"fakulitet av {p} er {summen}")
        #print("_-_-_-_-_-_-_-_-_-_-_-_")
        if summen == onsket:
            print(f"{onsket} er i fauliteten til {p} du er intelligent ")
            onske_oppfylt = True

if onske_oppfylt == False:
    print("Ønsket ditt ble ikke oppflylt......")