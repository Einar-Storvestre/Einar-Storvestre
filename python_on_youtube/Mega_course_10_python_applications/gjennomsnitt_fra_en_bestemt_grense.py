import time
new_list = []

def gjennomsnitt_for (a,b):
    print("HER KOMMER TALLENE:")
    time.sleep(3)
    for i in range(a,b+1):         #hvor mange prosent ferdig med tellingen
        print(f"{i} {(round(((i/b)*100),2))}%")
        new_list.append(i)
        if b > 60:
            time.sleep(a/(b/6))            #prosent andel av hele tallet slik at det alltid tar like lang tid
        else:
            time.sleep(a/b)
    return sum(new_list)/ len(new_list)


start_tall = int(input("Hva er det første tallet?: "))
slutt_tall = int(input("Hva er ord_tall grensen?: "))
antall_tall = slutt_tall+1 - start_tall


print("TELLING FERDIG:")
print(f"HER KOMMER RESULTATENE:\n Det var {antall_tall} tall og gjennomsnittet ble {gjennomsnitt_for(a=start_tall,b=slutt_tall)}.")
