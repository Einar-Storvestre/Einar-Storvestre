
masse = float(input("hovr mye veier du?: "))

arbeids_vei= float(input("hvor lange armer har du?:SKRIVES I 0,x-n meter: "))

energi_pullup = masse * 9.81 * arbeids_vei * 0.001 # blir da i newton meter f.eks 230 nm = 230 joule = 0.230 kilo joule . 0.1 fordi kilo joule

pullup_energi_brukt = 0

teller_antall = 0

what_messurement = str(input("måler du dette i kilo kalorier eller i kilo joule? SKRIV j FOR JOULE OG c FOR CALORIER: "))

if what_messurement == "c":
    kost_cal = int(input("hvor mage kilo calorier er inntaket ditt på?: "))
    print(energi_pullup)
    kilo_joule_kan_brukes = kost_cal * 4.1868 #får da kilo joule
    while kilo_joule_kan_brukes > pullup_energi_brukt:
        pullup_energi_brukt += energi_pullup
        teller_antall += 1
    print(f" Du greide {teller_antall} pullups IKKE FÅ TROEN PÅ DEG SELV DU ER ELENDIG EGENTLIG DETTE ER BARE TEORETISK:")
    print("""du må tenke på atp produskjon per glukose molekyl(varme stjeler), luft motstand, grep, muslklene du faktisk har osv""")

if what_messurement == "j":
    kost_cal = int(input("hvor mage kilo joule har du inntatt?: "))
    print(energi_pullup)
    kilo_joule_kan_brukes = kost_cal
    while kilo_joule_kan_brukes > pullup_energi_brukt:
        pullup_energi_brukt += energi_pullup
        teller_antall += 1
    print(f" Du greide {teller_antall} pullups. IKKE FÅ TROEN PÅ DEG SELV DU ER ELENDIG EGENTLIG DETTE ER BARE TEORETISK")

    print("""du må tenke på atp produskjon per glukose molekyl(varme stjeler), luft motstand, grep, muslklene du faktisk har osv""")

#else:
    #print("DU SKRIVER NOE FEIL: ERROR 420")
