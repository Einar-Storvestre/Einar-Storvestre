setning = ""

alphabet = dict(a="@", b="¨", c="¢", d="§", e="≈", f="´", g="'", h="-", i=">", j="*", k="+", l="h", m="<", n="l", o="“",
                p="$", q="(", r=")", s="?", t="!", u="#", v="%", x="|", y="\\", z="/", æ="`", ø="^", å="_",)

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
