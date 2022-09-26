5
gammel_pris = float(input("hva var den gamle prisen?: "))
prosent_okning = float(input("hvor mye har den steget med i prosent? (f.eks. 23 = 2,3%): "))
positiv_negativ = int(input("Er det økning eller nedgang?: "))

prosent_okning = prosent_okning / 1000 + 1
ny_pris = gammel_pris * prosent_okning



if prosent_okning <= 1:
    exit()

elif prosent_okning > 1:
    print(ny_pris)