from traceback import print_list


def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(10,20)

def calc_min(a, b):
    min = a - b
    print(min)
    return min

calc_min(10,30)

def calc_mul(a, b):
    mul = a * b
    print(mul)
    return mul

calc_mul(10,20)

def calc_div(a, b):
    div = a / b
    print(div)
    return div

calc_div(10,5)

def calc_mod(a, b):
    mod = a % b
    print(mod)
    return mod  

calc_mod(10,3)

def print_helo():
    print("helo")    

print_helo()    

def calc_avg(a, b, c):
    avg = (a + b + c) / 3
    print(avg)
    return avg

calc_avg(10,20,30)

def calc_area_of_rectangle(length, breadth):
    area = length * breadth
    print(area)
    return area

calc_area_of_rectangle(10,20)

def calc_fact(a):
    fact = 1
    
    for i in range(1, a+1):
        fact *= i
    print(fact)
    return fact

calc_fact(5)





def calc_usd_to_inr(usd):
    inr= usd * 95
    print(inr)
    return inr

calc_usd_to_inr(10)

def even_odd(num):
    num=int(input("enter a number:"))
    if num%2==0:
        print("even")
    else:
        print("odd")

even_odd(10)