
def h(x):
    return [i*2 for i in [1, x, 10]] #printer ut alle ord_tall ganget med 2

def g():
    return [i*2 for i in [1,4,10,-1] if i>0 ]    # printer ut alle ord_tall som er over 0 ganget med 2


print(g())


def q ():
    return [i*2 if i > 0 else 0 for i in [1,3,-4,-1]]    #hvis tallet er under 0 print 0

def p(x,y):
    return [i**2 for i in [x,y] if i>0 ]

print(q())

print(p(4,))