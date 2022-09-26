#def foo(*args):
   # return sum(args)/len(args)
#print(foo(liste))

liste =[]
while True:
    print("skriv \"hei\" for å avlutte..")
    raw_input = input(": ")
    if raw_input == "hei":
        break
    raw_input = int(raw_input)
    liste.append(raw_input)
liste_sum=sum(liste)
liste_len = len(liste)

def meen():
    return liste_sum/liste_len

print(meen())
