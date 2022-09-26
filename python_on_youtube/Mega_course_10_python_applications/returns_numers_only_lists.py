
new_list = []
def foo(data):
    for i in data:
        if isinstance(i,int):
            new_list.append(i)
    return new_list


foo([1,23,"hei" ,3,45])
print(new_list)