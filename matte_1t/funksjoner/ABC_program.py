a = float(input("skriv inn a: "))
b = float(input("skriv inn b: "))
c = float(input("skriv inn c :"))


under_rottegn = b**2 - 4*a*c

if under_rottegn >= 0: # to eller en løsning
    x1 = (-b + under_rottegn**(1/2))/(2*a)
    x2 = (-b - under_rottegn**(1/2))/(2*a)
    if under_rottegn == 0:         #hvis det er en løsning
        print(f"x1 = {round(x1,2)} ")
    else:       #da er det to løsninger
        print(f"x1 = {round(x2,2)} og x2 = {round(x1,2)}")
else:
    print("Det er ingen løsning")








