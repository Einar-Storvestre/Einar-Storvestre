setning = ""

alphabet = {"a": "@", "b": "8", "c": "(", "d": "|)", "e": "3", "f": "#", "g": "6", "h": "[-]", "i": "|", "j": "_|", "k": "|<",
            "l": "1", "m": "[]\\/[]", "n": "[]\\[]", "o": "0", "p": "|D", "q": "(,)", "r": "|Z", "s": "$", "t": "\'][\'" , "u": "|_|",
            "v": "\\/", "w": "\\/\\/", "x": "}{", "y": "`/", "z": "2",}

raw_input = input("")

for letter in raw_input:
    if letter == letter.upper():
        letter = letter.lower()
    if letter in alphabet:
        enslige = alphabet.get(letter)  # Return the value for key if key is in the dictionary, else default.
        setning += enslige
    else:
        setning += letter


print(setning)


# " ": " ", ".": ".", "!": "!", "?": "?", "'": "'", ",":",",