with open("hellopython/..terminal_over_the_wire")as myfile:
    content = myfile.read(90)  #de 90 første karakterene

print(content)

myfile.close()



with open("bear.txt.txt") as bear:
    content = bear.read()

with open("first.txt", "w") as first:
    content1 = content[:90]
    first.write(content1)

