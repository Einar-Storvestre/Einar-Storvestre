#strings are imutabel= can not be changed

my_string = "Hello World"

the_first_letter = my_string[0]
print(the_first_letter)

the_last_letter = my_string[-1]
print(the_last_letter)


substring = my_string[1:4]    #starts at index one to 4.   prints  index 1,2,3
print(substring)

substring2 = my_string[::2]   # prints every second letter
print(substring2)

substring3 = my_string[::-1]   # this is everything backwards
print(substring3)


for i in my_string:
    print(i)          #prints all letters in their own line


print(my_string.upper())
print(my_string.lower())

print(my_string.startswith("H"))    # does the string start with "H"?

print(my_string.find("ra")) # with index does this substring begin at, if its not there it returns -1


print(my_string.count("l"))    #how many l's are there?

print(my_string.replace('World', 'Universe'))   #if my_string contains "World" or "Universe" replace it.

my_string_for_list = "how are you doing?"
my_string_list = my_string_for_list.split(",")
print(my_string_list)




