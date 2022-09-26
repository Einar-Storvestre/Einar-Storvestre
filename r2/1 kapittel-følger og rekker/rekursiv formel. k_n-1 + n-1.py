antall_ledd = int(input("Antall a_1?: "))

ledd = 3 #a_1 a_1

start_verdi = 3    #det første leddet i følgen n=..

for n in range(start_verdi, antall_ledd + 1):
    print(f"Ledd nr. {n}:{ledd}")
    ledd += n    #husk at den blir n-1 siden den brukes i neste loop. "da blir den den forrige n'en."