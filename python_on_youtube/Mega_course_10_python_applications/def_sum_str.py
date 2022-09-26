new_list = []


def foo(data):
    for i in data:
        if isinstance(i,str):
            i = float(i)
            new_list.append(i)
        else:
            new_list.append(i)

    return sum(new_list)



foo(["1.3","1.5"])
print(sum(new_list))

#ELLER SLIK SOM DETTE:

#def foo(lst):
    #return sum([float(i) for i in lst])
