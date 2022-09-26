#import time

def f(x):
    return x**2+3*x-8


laveste_verdi = 200

p = -10

while p < 20:
    y = f(p)
    if y < laveste_verdi:
        laveste_verdi_x_kordinat = round(p,4)
        #print(y)
        laveste_verdi = y

    p += 0.01
    #time.sleep(0.01)

print(f" Dette er laveste verdi kordinater ({laveste_verdi_x_kordinat},{laveste_verdi})")
