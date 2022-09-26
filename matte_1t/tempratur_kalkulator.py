
F = input("hva vil du ha \"f\" eller \"c\"?: ")

if F == "c":
    antall_c = int(input("hvor mange celsius?: "))
    antall_F_svar = 9/5 * antall_c + 32
    print(f"det er {antall_F_svar}. farenheit. kult")

if F == "f":
    F = int(input("hvor mange farenheit?: "))
    c = (F - 32) / 1.8
    c = round(c, 1)
    print(f"det er {c}.celsius. kult")


