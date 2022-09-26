import random
navn1 = str(input("hvem er mannen?: "))
navn2 = str(input("hvem er jenten?: "))

antall_bokstaver = int(input("hvor mange tegn vil du ha?: "))
antall_bokstaver = antall_bokstaver /2
B = ""
A = ""

for count in range(int(antall_bokstaver)):
    A += (random.choice(navn1))
    B += (random.choice(navn2))


print(f"Barnet vil hete  {A+B}")
