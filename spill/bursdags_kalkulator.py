import datetime


today=datetime.date.today()
print(today)

print("hei og velkommen til einars tidsmaskin kalkulator: hvor mange dager må du reise for aa komme til akkurat ditt foodselsår??? ")
aar=input("hvilket år ble du født? ")
maaned=input("hvilke måned? ")
dag=input("hvilken dag (Dato)? ")

#luker vekk umulige verdier
if int(dag)> 31:
    dag = 31

   #finner ut hvilke år det er og luker vekk verdier


text1 = str(today)
ext1 = "-"

korrekt_aar = text1[:text1.find(ext1) + len(ext1)]
print(f"detter er året {korrekt_aar}")
#if int(aar)>2022:


##


#value = datetime.date(int(birthday[0]) + int(birthday[1]) + int(birthday[2]))
value = datetime.date(int(aar),int(maaned),int(dag))

print(value.strftime("du ble foodt: ""%B %d, %Y "))

dager_siden_du_ble_foodt= (today-value)
print(dager_siden_du_ble_foodt)

text = str(dager_siden_du_ble_foodt)
ext = " "

dager_siden_foodt_integer = text[:text.find(ext) + len(ext)]


dager_siden_du_ble_foodt = int(dager_siden_foodt_integer)


print(f"Det er {dager_siden_du_ble_foodt} dager siden du ble født")


timer_levd = (dager_siden_du_ble_foodt*24)
sekunder_levd = (timer_levd * 3600)


#mellomrom mellom tall i sekunder levd
forloup_teller =0
string_sekunderlevd = ""
print(string_sekunderlevd)

for tall in str(sekunder_levd):

    forloup_teller += 1

    if forloup_teller % 3 == 0:
        string_sekunderlevd += tall
        string_sekunderlevd += " "
    else:
        string_sekunderlevd += tall
##


print(f"{string_sekunderlevd} antall sekunder levd og {timer_levd} timer +- 12 timer , {int(dager_siden_du_ble_foodt)} uker siden")

print("-------------")

tusen_millon_millliard_trilliard_teller = 0
tall_teller = 0
for letter in str(sekunder_levd):
    tall_teller += 1
    if tall_teller % 3 ==0:
        tusen_millon_millliard_trilliard_teller += 1


if tusen_millon_millliard_trilliard_teller == 3:
    print("Dette er i milliard klassen")
elif tusen_millon_millliard_trilliard_teller == 4:
    print("Dette er i billon klassen")
elif tusen_millon_millliard_trilliard_teller == 5:
    print("Dette er i billiard klassen")
elif tusen_millon_millliard_trilliard_teller == 6:
    print("Dette er i trillion klassen")
elif tusen_millon_millliard_trilliard_teller == 7:
    print("Dette er i trilliard klassen")
elif tusen_millon_millliard_trilliard_teller == 8:
    print("Dette er i kvadrillion klassen")

print(f"Du har overlevd (timer) {timer_levd} timer av overlevelse. Det vil si (sekunder) {sekunder_levd} sekunder. \n wow det hadde du ikke trodd")

klokken=input("vil du vite hva klokken er? ")
if klokken == "ja" or "ok":
    print("klokken er akkurat i dette mikrosekud dette", (datetime.datetime.now()))


else:
    print("ok, Boomer")

