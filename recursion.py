def fact(a):
    if(a==0 or a==1):
        return 1
    return fact(a-1) * a
    
print(fact(5))

def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
   
show(5)    
def sum(n):
    if n==0:
        return 0
    return n + sum(n-1)
print(sum(5))

def print_list(list, idx):
    if idx==len(list):
        return
    print(list[idx])
    print_list(list, idx+1)
fruits = ["apple", "banana", "cherry"]
print_list(fruits, 0)