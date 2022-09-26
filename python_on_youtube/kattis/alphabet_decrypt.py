setning = ""

alphabet_decrypt = {"@": "a", "8": "b", "(": "c", "|)": "d)", "3": "e", "#": "f", "6": "g", "[-]": "h", "|": "i",
                    "|_": "j", "|<": "k",
                    "1": "l", "[]\\/[]": "m", "[]\\[]": "n", "0": "o", "|D": "p", "(,)": "q", "|Z": "r", "$": "s",
                    "\'][\'": "t", "|_|": "u",
                    "\\/": "v", "\\/\\/": "w", "}{": "x", "`/": "y", "2": "z", " ": " ", ".": ".", "!": "!", "?": "?",
                    "'": "'"}
raw_input = input("")

for letter in raw_input:
    print(letter)
    enslige = alphabet_decrypt.get(letter)  # Return the value for key if key is in the dictionary, else default.
    print(enslige)
    setning += enslige
    print(letter)


print(setning)
