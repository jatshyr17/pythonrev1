# type conversion
# a = 3
# b= 4.25
# # sum = a+b
# print(type(sum))
# a= int(input("enter the number ="))#because if we don't put int then the type of input will be string so yeah we have to type cast it to int or else the type of input will be string 
# b=int(input("enter the second number"))
# sum = a + b
# print("the sume of the two numbers is = ",sum)

# side = float(input("Enter the length of the side = "))
# area = side * side
# print(area)
# str = "this is a string"
# str1 = "this is the 2nd string"
# str2 = str + str1 
#slicing

#print(str[2:3]) positive indexing - 
#print(str[-3:-1]) negative indexing
# print(str[:5])
# print(str[4:])
#print(str[3:len(str)]) #to print letters till the end of the string if we doesn't know the end index of the string.
# a = str.endswith("ing") #to see if a string ends with a particular word 
# print(a)
# b = str.capitalize()
# print(b)
# c = str.replace( "string" , "float")
# print(c)
# d= str.find("string")
# print(d)

# e = input("enter the user's name = ")
# print(len(e))
# f=e.count("$")
# # to find the number of $s in a string
# print(f)

#conditional statements 

# age = int(input("enter the age = "))
# if(age>18):
#     print("can vote and apply for license")
# else:
#     print("cannot apply for license")
    
# if(age%2 == 0):
#     print("even")
# else:
#     print("odd")   

# a = int(input("Enter the 1st number "))
# b=int(input("Enter the 2nd number = "))
# c= int(input("Enter the 3rd number = "))

# if(a>b and a>c ):
#     print(a)
# elif(b>a and b>c):
#     print(b)
# else:
#     print(c)     

# d = int(input("Enter the number"))
# if(d%7 == 0):
#     print("true")
# else:
#     print("false")    

## LIST
# we can store items of multi data types 

rms = ["krish", "waqar","jatin","pundir","aman","ansh"]
# rms[5]="loki"
# print(rms) to change the element at an index
rms.append("loki")
print(rms)
rms.sort()
print(rms)
rms.sort(reverse = True)
print(rms)
rms.reverse()
print(rms)
rms.insert(2,"aditya")
print(rms)
rms.pop(3)
print(rms)

##TUPLES
#tuples are immutable just like string
tup=(1)
print(type(tup))
tup1=(1.098)
print(type(tup1))
#so from here we learn that in a single element tup when we use type of operator then the result will be the data type of the first element 
# to improve on this obstacle in tuples we just put a comma after the first element so that the type of operator results in tuple 
tup=(1,2,3,4,5,2)
print(type(tup))
print(tup.index(2))
print(tup.count(2))

### WAP to ask the user to enter names of their 3 fav movies & store them in a list 

movie1 = input("Enter the 1st movie:")
movie2 = input("Enter the 2nd movie = ")
movie3 = input("Enter the 3rd movie = ")
movie = []
movie.append(movie1)
movie.append(movie2)
movie.append(movie3)
print(movie)

## WAP to check if a list contains a palindrome of elements 

list1= [1,2,1]
copy_list= list1.copy()
copy_list.reverse()

if(copy_list==list1):
    print("palindrome")
else:
    print("no")
    
##WAP to count the number of students with the "A" grade in the following table

tup = ("c","d","a","a","b","a")

print(tup.count("a"))   

## wap to store the above values in a list and sort them from a to d
list =["c","d","a","a","b"]
list.sort()
print(list)


