x_kord = 0
y_kord = 0

def lengde (n): # i meter
    if n==0 :
        return 0
    return 1 * (0.9)**(n-1)


# annen hver vil listen ha like mange punkt i både x og y kordinat. derfor trenger vi ikke regne med hensyn på dette.
antall = 100

for i in range(1, antall+1):

    if i % 2==0:    # gjør at + og -'en blir riktig
        x_kord -= lengde(2*i-1)
        y_kord -= lengde(2*(i))
        print(f"({round(x_kord,3)},{round(y_kord,3)} etter a_{i} punkter")
    if i % 2 != 0:
        x_kord += lengde(2*i-1)
        y_kord += lengde(2*(i))
        print(f"({round(x_kord,3)},{round(y_kord,3)} etter a_{i} punkter")

print("############## \n")
print(f"sneglen går mot ({round(x_kord,3)},{round(y_kord,3)}).")