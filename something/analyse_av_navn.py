navn = input("hva er navnet?: ")

konsonantER = "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "z"
vokalER = ["a", "e", "i", "o", "u", "y", "æ", "ø", "å"]

kononant_teller = 0
vokal_teller = 0


for letter in navn:
    if letter in konsonantER:
        kononant_teller+=1
    if letter in vokalER:
        vokal_teller+=1



print(f"du har {kononant_teller} konsonater i navnet ditt, og {vokal_teller} vokaler i navnet ditt")