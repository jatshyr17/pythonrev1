
# n=int(input("Enter the number = "))
# for i in range(11):
#     print(n*i)

# name = "jatin"
# age = 21
# price = 14.5
# print(type(name))
# print(type(age))
# print(type(price))
# a,b=2,3
# txt="@"
# print(a*txt*b)
# print(txt,a/b,a//b,a+b,a-b,a*b)
# print(2**3)

# age = int(input("Enter the age ="))
# if(age >= 18):
#     print("adult or eligible to vote")
# else:
#     print("not eligible to vote or not adult")
    
# light = input("which light it is:")
# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("invalid light color")    

# ternary operator
food = input("food :")
eat="yes" if food == "cake " else "no"
print(eat)

print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")

#clever if
sal= int(input("Enter your salary = "))
tax = sal *(0.1,0.2) [sal<=50000]
print(tax)