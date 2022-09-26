

oddetall = {1 ,3 ,5 ,7 ,9}
partall = {2 ,4 ,6 ,8}
primtall = {2, 3, 5 ,7}

union = oddetall.union(partall)            #prints both of the sets in numeretic order
print(union)

inersection = partall.intersection(primtall)       #elements found in both sets   # here only the even primenumbers gets printed
print(inersection)


print("------------") #skille

set1 = {1,2,3,4,5,6,7,8,9}
set2 = {1,2,3,10,11,12,13}

diff = set1.difference(set2)      #hva er forskjellig mellom stene. printer ut de som ikke er like
print(diff)

set1.update(set2)           #there is no duplicates in sets. even when we add other sets together with same numbers
print(set1)


set1.intersection_update(set2)          #updates the sets keeping only the values in both sets
print(set1)

set1.difference_update(set2)           #updates the set removing the mutual values. prints then the difference

set1.symmetric_difference_update(set2)   #updates the set by only keeping the elements different values in both sets.

print(set1.issubset(set2))      #tells if all the element in set1 is in set2   #ture or false statement
print(set2.issubset(set1))

print(set2.issuperset(set1))    # superset is true if the first set containes all the elements from the second set

i = frozenset([1,2,3,4])      #can not be changed  with remove or addd, but union and other methods work.


