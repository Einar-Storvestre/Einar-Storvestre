
def f(x):
    return x**3-2*x+1

s = -2   #start verdi
t = 2 #sluttverdi
leggertil = 0.001 #bestemmer hvor mye nøyaktighet

while s < t:  # går gjennom alle tall mellom start og slutt verdi med 0.
    if abs(f(s))<0.001:   # absolute value (fordi + og minus) av funksjonen er midre 0.001
        print(f"nullpunktet er ved x ={s}")  #hvis så er det et nullpunkt
    s += leggertil


