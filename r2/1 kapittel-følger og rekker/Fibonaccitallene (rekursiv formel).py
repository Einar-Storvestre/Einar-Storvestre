


antall_ledd = int(input("Antall a_1?: "))

ledd = 1    # a_1 a_1

ledd_2 = 0  # a_n-2

diff = 0 # differanse. brukes til å finne hvor mye leddene øker med

for n in range(1, antall_ledd + 1):
    print(f"Ledd nr. {n}:{ledd}")

    ledd = ledd_2 + ledd   #her bruker koden det forrige leddet ("a_1" er det forrige leddet), det kan du legge til eller gange (osv) for å få neste a_1.

    diff = ledd - ledd_2  # finner ut hvor mye leddet øker med, tar da vekk det den øker med for å få den forrige verdien, a_n-2.

    ledd_2 = diff  # ledd_2 blir til a_n-2 ved hjelp av diff.

