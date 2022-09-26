i = 1
teller = 0
maks_grense = int(input("hva er grensen?: "))
while i ** 3 < maks_grense:
    print(i ** 3)
    i += 1
    teller += 1

print(f"{teller} ^3 = nærmeste kubikktall under {maks_grense}")
