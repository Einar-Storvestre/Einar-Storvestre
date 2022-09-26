import random

gjettning = input("gjett det tilfeldige tallet mellom 1 og 10: ")


def mastermind ():
    return random.randint(1, int(2))


print(mastermind())

if gjettning == mastermind():
    print("kult")

else:
    print("feil")