import random
import time
import datetime

antall_vunnet = 0
antall_provd = 0
alle_riktige_bokstaver_for_score = 0

i_dag = datetime.date.today()

kastes_ut = False


def hangman(antall_vunnet, alle_riktige_bokstaver_for_score, kastes_ut):

    liste_av_gjettede_ord = []

    antall_lovlige_feil = 10

    bokstaver_gjettet_feil = 0
    bokstaver_gjettet_rikitg = 0

    ord_liste = ["penal", "knut", "einar", "athene","katt","hund","trekkspill","hus","mus","automobil","datamaskin","koding","seriøsitet","bilde"] #FINNE GJETTE ORD #lag et dictonary med hint om ordet som printes ut

    ord_tall = random.randint(0, len(ord_liste)-1)
    gjette_ord = ord_liste[ord_tall]
    gjette_ord_string= gjette_ord

    visuel_ord_linje = len(gjette_ord) * "_"         #string
    faktisk_lengde = len(gjette_ord)
    #print(gjette_ord)
    visuel_ord_linje = list(visuel_ord_linje)         #LAGER LISTER OG VISUELLE LINJER
    gjette_ord = list(enumerate(gjette_ord))      #liste med tupels


                                          # lage loading screen f.eks 10 % load osv.
    for i in range(1,100+1):
        if i%10==0:
            print(f"{float(i)}%  Loading....")
            time.sleep(i/100)
    print("\n"*3)
    print("KLAR.")






    print(f"HEI, og velkommen til HANGBOY... \n ...\n REGLENE ER SIMPLE: \n1) Ordet er {faktisk_lengde} bokstaver langt."
        f" \n2) Du kan gjette opptil {antall_lovlige_feil} feil. "
        f" \n3) Skriv bare inn små enkeltbokstaver. "
        f" \n4) Ha det gøy....")




    print(visuel_ord_linje)



    while True:
        if bokstaver_gjettet_rikitg == faktisk_lengde:     # alle er gjettet
            print("DU GREIER ALT MIN VENN")
            antall_vunnet += 1
            break

        raw_input = input("Hvilken bokstav?: ")

        if raw_input in liste_av_gjettede_ord:  #hvis gjenntagende gjetting
            raw_input = input("Det har du gjettet. gjett igjen: ")
        liste_av_gjettede_ord.append(raw_input)

        if raw_input in gjette_ord_string:  #RIKITG GJETTET
            for i, letter in gjette_ord:
                if letter == raw_input:
                    bokstaver_gjettet_rikitg += 1
                    alle_riktige_bokstaver_for_score += 1
                    visuel_ord_linje[i] = letter        #ENDRER DET VISUELLE
                    print(visuel_ord_linje)

        if bokstaver_gjettet_feil == antall_lovlige_feil-1:   #ser om du er tom for sjanser
            print(f"SÅ LANGT KOM DU: {visuel_ord_linje} ")
            print(f"PS: Det rikige ordet var {gjette_ord_string}")
            kastes_ut = True
            break

        if raw_input not in gjette_ord_string:
            bokstaver_gjettet_feil +=1
            print(f"DET ER FORTSATT HÅP... DU HAR {antall_lovlige_feil-bokstaver_gjettet_feil} FORSØK IGJEN")


    print(f"du gjettet {alle_riktige_bokstaver_for_score} bokstaver riktig")

    return antall_vunnet,alle_riktige_bokstaver_for_score, kastes_ut

# MENY
print("hei og velkommen: ")
navn = input("Hva skal vi kalle deg?: ")
while True:
    meny_interaktiv = input("hva vil du gjøre \n 1) scoreboard \n 2) spille \n 3) avslutte \n SKRIV INN ØNSKET NUMMER: ")
    if meny_interaktiv == "1":

        with open("Scoreboard_hangman") as Scoreboard:
            les_scoreboard = Scoreboard.read()

        print(les_scoreboard)
        Scoreboard.close()
        meny_interaktiv = input("hva vil du gjøre \n 1) scoreboard \n 2) spille \n 3) avslutte \n SKRIV INN ØNSKET NUMMER: ")

    ikke_igjen = False  #tillhørende om du vil spille igjen eller ikke når du allerede har vunnet

    if meny_interaktiv == "2":  #spille


        a,b,c= hangman(antall_vunnet,alle_riktige_bokstaver_for_score,kastes_ut)
        print(antall_vunnet)

        antall_vunnet = a
        alle_riktige_bokstaver_for_score = b
        kastes_ut = c

        while not kastes_ut and ikke_igjen == False:  #kastes_ut == false:    #så lenge du ikke er tom for sjanser
            print(f"du har gjettet {alle_riktige_bokstaver_for_score} bokstaver riktig")
            print("Du kan få fortestte vinnerrekken: ")
            print(f"{navn} har vunnet {antall_vunnet} ")
            igjen_sporsmol = input("VIl du spille gjen? ja/nei: ")

            if igjen_sporsmol == "ja":
                a, b, c = hangman(antall_vunnet, alle_riktige_bokstaver_for_score, kastes_ut)
                print(antall_vunnet)

                antall_vunnet = a
                alle_riktige_bokstaver_for_score = b
                kastes_ut = c



            if igjen_sporsmol=="nei":
                meny_interaktiv = "3"  # til avsluttningsmeyen (3)
                ikke_igjen = True
                print("hade")



        if kastes_ut == True:
            print(f"{navn} har dessverre tapt med scoren {antall_vunnet}, og gjettet {alle_riktige_bokstaver_for_score} riktige bokstaver")
            meny_interaktiv="3"  #til avsluttningsmeyen


    if meny_interaktiv == "3":  #avbryte
        print("takk for tiden, hade")
    with open("Scoreboard_hangman","a") as scoreboard:
        scoreboard.write(f"{navn}, {antall_vunnet} vunnet, {alle_riktige_bokstaver_for_score} bokstaver riktig, dato: {i_dag} \n ")

        break



print("Du kan få lov til å spille på nytt, uansett fortell programutvikleren \nom opplevelsen din")




#tilbakemeldinger tekst fil

