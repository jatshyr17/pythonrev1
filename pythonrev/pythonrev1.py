# from pythonrev import chai 

# chai("ginger tea")
# my_list =['python','c','java']
# my_list.append('go')
# print(my_list)
# my_list_copy = my_list.copy()
# print(my_list_copy)
# my_list_copy.insert(1,'js')
# print(my_list_copy)
# my_list_copy.pop()
# print(my_list_copy)
# print(len(my_list_copy))
# sqr_nums = [x**2 ]

# print(range(10))

# for i in range (0,10):
#     print(2*i)
   
# sqr_numbers = [ x**2 for x in range(0,10)]
# print(sqr_numbers)  

chai_types={"Masala":"spicy","Ginger":"Zesty","Green":"Mild"}

print(chai_types)

print(chai_types["Masala"])

print(chai_types.get("Ginger"))
chai_types["Green"] = "Fresh"
print(chai_types)

for chai in chai_types:
    print(chai,chai_types[chai])
    
for key , value in chai_types.items():
    print(key,value)    
    
if 'Masala' in chai_types:
    print("i have masala chai")
pop = chai_types.pop("Ginger") 
print(pop)   
    
print(chai_types.popitem())    
chai_types["hello"] = 'jatin'

print(chai_types)
tea_shop = {
    "chai":{"Masala":"Spicy","Ginger":"Zesty"},
    "Tea":{"Green":"Mild","Black":"Strong"}}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])

sqr_num = {x:x ** 2 for x in range(10)}
print(sqr_num)

key = ["Masala","Ginger","Lemon"]
print(key)
default_value = "Delicious"
new_dict=dict.fromkeys(key,default_value)
print(new_dict)

