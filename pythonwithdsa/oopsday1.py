#creating class 
class student :
    
    def __init__(self, fullname,marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in Database..")
   
    
#creating object(instance)
s1 = student("karan",97)
print(s1.name , s1.marks)


# #constructor is basically the __init__ function which is executed when a class is initiated 

# class jatin:
#     name = "jatin sharma"
#     age = 21 
    
# j1= jatin()
# print(j1.name)

# class student:
    
#     def __init__(self,marks,name):
#         self.name = name
#         self.marks = marks
        
#     def get_avg(self):
#         sum = 0
#         for num in self.marks:
#             sum += num
#         print("hi", self.name,"your avg score is:",sum/3)    
# s1=student("jatin",[99 ,98 ,97])     
# s1.get_avg()

# class Account:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no=acc
        
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs",amount,"was debited")
#         print("total balance=",self.get_balance())

#     def credit(self,amount):
#         self.balance += amount
#         print("Rs",amount,"was credited")
#         print("total balance=",self.get_balance())
            
#     def get_balance(self):
#         return self.balance    
            
# acc1=Account(10000,12345)
# acc1.debit(1000)
# acc1.credit(2345)
# print(acc1.balance)
     
