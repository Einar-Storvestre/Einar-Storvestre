import random


sider =int(input("hvor mange sider?: "))
antall = int(input("hvor mange ganger?: "))

for i in range(antall):
    print(random.randint(1,sider))


