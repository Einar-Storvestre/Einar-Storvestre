import random
antall_bokstaver = input("hvor mange tegn vil du ha?: ")
A = ""

for letter in range(int(antall_bokstaver)):
    A+=(random.choice('ÆØÅ1234567890+?.,qwertyuioplkjhgfdsazxcvbnm'))



print(A)



