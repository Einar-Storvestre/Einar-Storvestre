import json

data = json.load(open("data.json"))


while True:
    ord1 = input("hvilket ord lurer du på?: ")
    ord1 = ord1.lower()
    ord1 = ord1.strip()

    def definisjon (ord1):

        if ord1 in data:   #hvis det finnes
            vellykket_definisjon = data[ord1]

            forloup_teller = 0
            string_definisjon = ""

            for bokstaver in vellykket_definisjon:        #120

                forloup_teller += 1

                if forloup_teller % 120 == 0:
                    string_definisjon += bokstaver
                    string_definisjon += "\n"
                    print("HHHHH")
                else:
                    string_definisjon += bokstaver
            print(forloup_teller)
            print(string_definisjon)        ##output
        else:           #hvis det ikke finnes
            print("Dette ordet er ikke i ordlisten")


    print(definisjon(ord1))
    igjen = input("Skriv 'om igjen' for å fortsette \nVilkårlig bokstav for å avslutte\n: ")   #vil du spille igjen
    if igjen != "om igjen":
        break


