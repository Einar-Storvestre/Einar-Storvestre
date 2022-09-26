x = input()
while x != "exit":
    x = int(x)
    y = 0
    z = x
    while z != 0:         #opphøyer i tall i 3
        y += x
        z -= 1
        if z <= 0:
            y *= x
    print(y)
    x = int(input())

print('You chose to end the program, goodbye!')
