# oppgaven: du skal printe n n statuer, hvor mange dager tar det?
# en printer kan printe en ny printer eller en ny staue, per dag

statuer = int(input("hvor mange statuer?: "))
statu_teller = 0
antall_printere = 1
dager = 0


while antall_printere < statuer:#printere er lønnsomt
    dager += 1
    antall_printere = antall_printere*2
    print(f"{antall_printere} printere.. {dager} dager.")

while statu_teller < statuer:
    dager+=1
    for i in range(antall_printere):
        statu_teller += 1

print(f"Det tok {dager} dager å lage {statuer} statue(r). Da brukte einar__industies__ {antall_printere} printere")

