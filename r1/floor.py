
from math import floor
svar = input("Oppgi et tall a:")
a = float(svar)

if floor(a) == a:
    print("Tallet", svar , "er et helt tall.")

if floor(a/2) == a/2:
    print("Tallet", svar, "er et partall.")
else:
    print("Tallet er ikke et helt tall.")

if a % 2 != 0:
    print("det er et oddetall")


   # tall = input("hvilke ord_tall tenker du på?: ")
    #tall = int(tall)
    #if tall % 2 == 0:
    #    print(f"tallet {tall} er et partall")
   # else:
     #   print(f"tallet ditt ({tall}) er et oddetall")