balance = int(input("hvor mye starter du med?: "))
onsket_balance = int(input("hvor mye vil du ende opp med?: "))
inskudd = int(input("hvor mye vil du sette inn hver år?: "))
vekstfaktor = int(input("hilken rente / vekstprosent har du?(oppgis som heltall. f.eks 2,3 % = 23): "))
vekstfaktor = vekstfaktor/1000 + 1
tid = 0

while balance < onsket_balance:
    balance = balance * vekstfaktor + inskudd
    tid += 1

print(" \n ")
balance = round(balance,1)
print(f"""Etter {tid} år med {inskudd} kr satt in på konto hvert år,
\n og med {vekstfaktor} prosent i rente/vekstfaktor.\n Får du {balance} kr i banken """)