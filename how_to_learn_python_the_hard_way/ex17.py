from sys import argv
from os.path import exists
script, from_file, to_file = argv
print(f"copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long")

print(f"does the output file exist? {exists(to_file)}")
print(f"ready, hit return to continue, CTRl-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("alright, all done ")
out_file.close()
in_file.close()

#hvrdan lage en ny fil og skrive i den i en linje i terminal? skriv: "echo "blbalbalbal" > ny_fil.txt
#koden kopierer en fil sitt innhold til en annen


