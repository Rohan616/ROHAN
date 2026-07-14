list = (1,4,9,16,25,36,49,64,81,100)
x=49

idx=0
for num in list:
    if(num==x):
         print("the num is found at index",idx)
         break
    idx+=1
else:
    print("The loop is over")