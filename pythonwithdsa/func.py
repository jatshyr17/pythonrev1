#FUNCTIONs
def Sum(a,b):
    sum = a + b 
    print(sum)
    return sum

Sum(3,4)    
    
def avg(a,b,c):
    avg = (a+b+c)/3
    print(avg)
    return avg
avg(6,7,10)    

#Functions are of two types built in and user defined
# Built-in : print(),len(),type(),range()
# user defined: jo mai define karunga jaise upper kiye h 

list = [ 1,2,3,4,5,6,7,8]
def print_len(list):
    print(len(list))
    
print_len(list)    

def items_list(list):
    for i in list:
     print(i,end="")
items_list(list)    
 
def fact(a):
    
    
    fact=1
    for i in range(1,a+1):
        fact*=i 
        print(fact)
        
fact(5)        

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
fact(5)    