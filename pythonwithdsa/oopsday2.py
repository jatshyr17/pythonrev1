# class student:
    
#     def __init__(self , name):
#         self.name = name
        
# s2 = student("shradha")
# print(s2.name) 

class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped")
        
class ToyotaCar(Car):
    def __init__(self,brand,type):
        self.brand = brand
        super().__init__(type)
        super().start()
        
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type
        
        super
        
car1 = Fortuner("diesel")
car1.start()               
        
        
            
                
    
       