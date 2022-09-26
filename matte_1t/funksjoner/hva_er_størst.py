

raw_input3 = int(input("Hvilke ord_tall?: "))
raw_input2= int(input("Hvilke ord_tall?: "))
raw_input1 = int(input("Hvilke ord_tall?: "))

biggest = raw_input1

my_list =[raw_input2,raw_input3,raw_input1]



def hei():
    for i in my_list:
        if biggest < i:
            biggest = i


print(biggest)