

def foo(*args):
    liste = []
    for args in args:
        liste.append(str.upper(args))
    liste = sorted(liste)
    return liste




print(foo("hei","katt","frank"))