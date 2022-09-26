import numpy as np

#a = float(input("Skriv inn lengden til side 1:" ))
#b = float(input("Skriv inn lengden til side 2:" ))
#c = float(input("Skriv inn lengden til side 3:" ))
b=88
c=115    #dette er de to sidelengdene

a = 140
while a<15:

    cosinus_verdi_vinkel = np.arccos((a**2-b**2-c**2)/(-2*b*c))  #cosinus verdi i radianer


    vinkel_i_grader = np.rad2deg(cosinus_verdi_vinkel)  # vinkel_i_grader = vinkel A


    sinus_verdi_av_vinkel_i_grader = np.sin(np.deg2rad(vinkel_i_grader))  # sinus verdien av radianene i grader



    areal = 0.5*b*c*sinus_verdi_av_vinkel_i_grader
    #print(areal)
    if areal < 17.7:
        if areal>17.4:
            print(f"{a}er sidelengden")

    a+=0.1

print(f"{areal} er arealet til trekanten din:)69! ")





