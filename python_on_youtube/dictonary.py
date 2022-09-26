# dictonary is unordered , mutable, key-value pairs who have an assosiated value
import sys

my_dictonary = {"name": "einar", "age": 15, "city": "bergen", "dogsname": "athene"}  # alt + shift 8 for disse {}

my_dictonary2 = dict(name="einar", age=15, city="bergen", dogsname="athene")

print(my_dictonary)
print(my_dictonary2)

print(sys.getsizeof(my_dictonary), "bytes in ordinary dictonaty")
print(sys.getsizeof(my_dictonary2),
      "bytes in high level code dictonary")  # bruker like mye plass  , så det er det samme

value = my_dictonary["age"]  # prints my age
print(value)

try:
    print(my_dictonary["name"])
except:
    print("ERROR")

for key in my_dictonary:
    print(key)     #alle spørsmålene

print("\n THIS IS THE VALUES IN THE KEY-VALUE PAIRS\n")

for value in my_dictonary.values():
    print(value)

for key, value in my_dictonary.items():        #prints everything
    print(key, value)

