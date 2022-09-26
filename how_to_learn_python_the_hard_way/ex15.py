from sys import argv
script, filename = argv
txt = open(filename)

print(f"here is your file {filename}:")
print(txt.read())

print("type in filename again:")
file_again=input(">")

txt_again = open(file_again)
print(txt_again.read())


#du må lage en ny fil so du kan lese eller en du har da f.eks ex15_read_file.txt