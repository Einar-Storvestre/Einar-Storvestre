#input = sidene på rektangelet
#output = hvor store de små kvadratene makismal kan være.
teller_store_kvadrat= 1
sma_bokser_teller = 0


raw_lengde = int(input("hvor lang er den?: "))
raw_bredde = int(input("hvor bred er den?: "))

areal_hele = raw_lengde * raw_bredde
store_kvadrat = raw_bredde ** 2

areal_igjen = areal_hele - store_kvadrat

konstand_storekvadrat = store_kvadrat

while areal_igjen >= store_kvadrat:
    store_kvadrat += konstand_storekvadrat
    teller_store_kvadrat += 1

ekstra_stripe = areal_hele - store_kvadrat

print(f"")

ekstra_stripe_lengde = ekstra_stripe / raw_bredde


print(f"""Antall store kvadrat {teller_store_kvadrat} og hva er igjen som en stripe {ekstra_stripe} stripen er {raw_bredde} høy og {ekstra_stripe_lengde} lang""")
print("--------------")
print(store_kvadrat)
#if store_kvadrat != areal_hele:
sma_bokser_teller = 1
liten_boks = ekstra_stripe_lengde ** 2
liten_boks_samlet_areal = liten_boks * sma_bokser_teller
while ekstra_stripe > liten_boks_samlet_areal:
    sma_bokser_teller += 1


stripe_areal_igjen = ekstra_stripe-(sma_bokser_teller * liten_boks)
print(stripe_areal_igjen)
print(f"antall små bokser er {sma_bokser_teller} boksene er {liten_boks} store.  Da er det {stripe_areal_igjen} areal igjen" )#som skal deles på ekstra_stripe_lengde

if store_kvadrat == areal_hele:
    print(f"{store_kvadrat} er største mulige kvadrat")