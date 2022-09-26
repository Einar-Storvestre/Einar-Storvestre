setning = ""

alphabet = {"@":"a","¨":"b","¢":"c", "§":"d", "≈":"e", "´":"f", "'":"g", "-":"h", ">":"i", "*":"j", "+":"k", "h":"l", "<":"m", "l":"n", "“":"o",
                "$":"p", "(":"q", ")":"r", "?":"s", "!":"t", "#":"u", "%":"v", "|":"x", "\\":"y", "/":"z", "`":"æ", "^":"ø", "_":"å"," ":" ", ".":".",}


raw_input = input("")

for letter in raw_input:
    enslige = alphabet.get(letter)  # Return the value for key if key is in the dictionary, else default.
    setning += enslige

print(setning)
