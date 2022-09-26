sum = 0

antall_aar = 12

rente = 1.03

start_innskudd = 10000

for n in range(1, antall_aar + 1):
  sum += start_innskudd * rente**(n-1)

print(f"Etter {antall_aar} år har Mari {sum :.2f} kr.")