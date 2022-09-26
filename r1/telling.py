import time
start_time = time.time()


count = 1
while count < 1000000:
    count += 1
    print(count)
for i in range(1000000):
    print(i)

print("--- %s seconds ---" % (time.time() - start_time))