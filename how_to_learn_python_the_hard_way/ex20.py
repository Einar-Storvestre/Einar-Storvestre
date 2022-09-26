from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("lets print the whole file!: \n")

print_all(current_file)

print("now lets rewind \(spill på nytt tror jeg\) ")

rewind(current_file)

print("lets print out three lines: ")

current_line = 1


for current_file in range(3):
    print_a_line(current_line)





