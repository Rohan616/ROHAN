num = (1,4,9,16,25,36,49,64,81,100)
 
x = 1
i = 0
while i<len(num):
    if num[i] == x:
        print("Found at index:", i)
        break
    i += 1
else:
    print("Not found")
