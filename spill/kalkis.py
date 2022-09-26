num1 = input("skriv inn et tall: ")
num2 = input("skriv inn et annet tall: ")
hva = input("vil du gange, dele, addere eller subtraere?: ")
if hva == "gange":
    resultat = float(num1) * float(num2)
elif hva == "dele":
    resultat= float(num1)/ float(num2)
elif hva == "addere":
    resultat = float(num1) + float(num2)

else:
    resultat = float(num1) - float(num2)







print(resultat)
