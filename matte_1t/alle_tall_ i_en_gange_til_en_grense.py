gange_tabell = int(input("hvilken gangetabell?: "))
grensen = int(input("hva er grensen?: "))
teller = -1
for i in range(grensen):
    if i % gange_tabell == 0:
        print(i)
        teller += 1

print(f" {gange_tabell} * {teller} = ^ tallet ovenfor")

#for i in range(1, 201):
    #if i % 7 == 0:            eller slik som dette
        #rint(i)