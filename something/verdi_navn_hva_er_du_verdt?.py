import datetime
i_dag=datetime.date.today()

bokstaver_dictonary = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,
                       "l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"æ":27,"ø":28,"å":29}

#mål
# legge sammen key-valuene til bokstavene

#hvordan
# for loop av input legger til key-valuene til en tom variabel som printes ut til slutt

navn_verdi = 0

navn = input("Navn: ")

for letter in navn:
    if letter.isupper():   #gjør alle bokstaver til små-bokstaver
        letter = letter.lower()

    if letter in bokstaver_dictonary:
        navn_verdi += bokstaver_dictonary[letter]   #legger til key-valuen til variabelen

def high_score_fil(navn,i_dag,navn_verdi):
    high_score = open("navn_highscore","a")
    high_score.write(f"{navn} score: {navn_verdi} dato: {i_dag} \n") #dette skrives inn i high_score filen
    #high_score.seek(0)
    high_score.close()

print(high_score_fil(navn,i_dag,navn_verdi))

print(f"Du har en verdi på {navn_verdi}")


