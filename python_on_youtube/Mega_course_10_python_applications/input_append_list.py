new_list = []


def foo(data):
    for i in data:
        if i > 0:
            new_list.append(i)
    return new_list


foo([1,4,65,-3,-5])

print(new_list)