# oppgaven: du skal printe n n statuer, hvor mange dager tar det?
# en printer kan printe en ny printer eller en ny staue, per dag

statuer = int(input("statuer: "))
statu_teller = 0
antall_printere = 1
dager = 0


while statuer > statu_teller:# kjører koden hver dag
    for i in range(antall_printere+1):              # kjører koden etter hvor mange printere som eksister
        while statu_teller + 2 < statuer:       #lag ny printer
            antall_printere += 1
            dager += 1
            if antall_printere*2 >= statuer:
                break
        if statu_teller < statuer:#printer en ny statue
            while statu_teller < statuer:
                dager += 1
                statu_teller += 1


print(f"Det tok {dager} dager å lage {statuer} statue(r).")
