import random


print("trille trening")

#input("hvor mange sider: ")
antall = input("hvor mange sider: ")
hvormage=input("hvor mange vil du trille: ")



def trille_terning(antall):
    return random.randint(1,int(antall))

for i in range(int(hvormage)):
    print(trille_terning(antall))


