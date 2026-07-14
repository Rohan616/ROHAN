list1=[1,2,8,7,2,1]
list2=list1.copy()
list2.reverse()
print(list2)
if list1==list2:
    print("list1 is palindrome")
else:
    print("list1 is not palindrome")