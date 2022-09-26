def oversette (setning):
    oversettelse=""
    for bokstav in setning:
        if bokstav.lower() in ("aeiouæøå"):
            if bokstav.isupper():
                oversettelse = oversettelse + "X"
            else:
                oversettelse = oversettelse + "p"
        else:
            oversettelse = oversettelse + bokstav
        #oversettelse= oversettelse+bokstav
    return oversettelse

print(oversette(input("hva vil du oversette til einisisspråkis? ")))




