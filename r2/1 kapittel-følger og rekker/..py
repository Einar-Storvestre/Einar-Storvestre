sum = 0
i=1

while sum < 10:
    if int(sum) < int(sum+1/i):
        print("Ledd nr.", int(sum)+1, "er", i)
    sum += 1/i
    i+=1




