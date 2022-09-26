#u = r * E hva er spenning
stromstyrke = float(input("hva er strømstyrken?: "))
spenning = float(input("hva er spenningen?: "))


motstand = spenning / stromstyrke
motstand = round(motstand, 2)
print(f"motstanden er {motstand}")



