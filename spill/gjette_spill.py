from PIL import Image

secret_word ="gorilla"
guess=""
guess_count=0
guess_limit=3

out_of_guesses=False
svar= "einar er best"
print("VELKOMMEN til einars gjettespill, du kan svare tre ganger")
svar_fra_bruker = input("skriv : \"einar er best\" : for å delta ")
if svar_fra_bruker ==svar:
    print("ok du kan spille")
else:
    print("nei du får ikke adgang")
    exit()

print("svaret er et strort dyr i jungelen, som kan klatre og er inteligent ")


while guess != secret_word and not ( out_of_guesses ):
    if guess_count>0 and guess_count<=3 :
        print("prøv på nytt")
    if guess_count< guess_limit:
        guess= input("Skriv inn ditt svar: ")
        guess_count+= 1

    else:
        out_of_guesses=True
if out_of_guesses:
    print("Du har ikke flere svar igjen, DU ER EN TAPER")
else:
    print("DU VINNER! gratulerer. håper du ikke får korona. ha en fin dag")







