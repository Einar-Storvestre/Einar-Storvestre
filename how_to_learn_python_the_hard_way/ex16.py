from sys import argv
script, filename = argv
print(f"we are going to erase {filename}.")
print("if you don´t want that, press CTRL-C (^C). \n if not press press Return: ")

input("?")

print("opening the file.... ")
target = open(filename, 'w')
print("destorying all material (truncating) the file. lol. bye bye")
target.truncate()

print("now i'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("i´m going to write these to the file.")

target.write(f"{line1} \n {line2} \n {line3} \n")
print("yeah, finally, we close it")
target.close()


