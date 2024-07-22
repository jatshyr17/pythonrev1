#while loop
#print numbers from 1 to 100

# i=1
# while i<=100:
#     print(i)
#     i+=1
    
#print numbers from 100 to 1

# i = 100
# while i>=1:
#     print(i)
#     i-=1   

#print the multiplication table of a number 

# n=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(n*i,i)
#     i+=1

#print the elements of the following list using a loop 

# l =(1,4,9,16,25,36,49,64,81,100)
# x=36
# i = 0
# while i<len(l):
#     if(l[i]==x):
#         print("yes",i)
#         break
#     else:
        
#         print("no")
#     i+=1
    
# #continue
# i = 0
# while i <=5:
#     if(i == 3):
#         i+=1
#         continue
#     print(i)
#     i+=1
    
    
l = (1,4,9,16,25,36,49,64,81,100)
# for val in l:
#     print(val)
x = int(input("enter the number:"))
i=0
for el in l:
    if(el == x):
        print("found",i)
    
    