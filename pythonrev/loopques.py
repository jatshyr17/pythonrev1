# num = [1,-2,3,-4,5,6,-7,-8,9,10]
# positive = 0

# for i in range(len(num)):
#     if num[i] >0:
#         positive +=1
#     else:
#         print("negative")
        
# print(positive)    

# n = int(input("Enter the limit number :"))
# sum = 0
# for num in range (0,n):
#     if num%2 == 0:
#         sum += num
# print(sum)  

      
      
# number = int(input("Enter the number:"))
        
# for i in range (10):
#     if i == 5:
#         continue
#     print(number*i)            
# str = input("Enter the string")
# reverse = ""
# for char in str:
#     reverse = char + reverse
# print(reverse)    

input_str = "teeteracdacd"
for char in input_str:
    if input_str.count(char)==1:
        print("Char is:",char) 
        break
                         