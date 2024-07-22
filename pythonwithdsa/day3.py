# # import math as m 
# # a = int(input("Enter the 1st number = "))
# # b = int(input("Enter the 2nd number = "))
# # c = m.pow(a,b)
# # print(c)

# #DICTIONARY
# #Dictionary are used to store data values in key:value pairs
# #they are unordered ,mutable (changeable) & don't allow duplicate keys 

# info = {
#     "name" : "apna college",
#     "subjects": [ "math","english","science"],
#     "topics" : ("dict" , "set"),
#     "age" : 35,
#     "is_adult": True,
#     45 : 78.5
#     }
# print(info)
# print(type(info))
# print(info["name"])
# info["name"] = "jatin"
# info["surname"]="ekta"
# print(info)

# # to create a null dictionary 

# null_dict={}
# null_dict["name"]= "apnacollege"
# null_dict["skills"] =["c" , "c++" , "python" , "java"]
# print(null_dict)

# #nested dict works like nested list the only exception is in this we make a key a dict .

# info = {
#     "name":"jatin",
#     "score": {
#         "phy" : 89,
#         "chem" : 78, 
#         "math" : 99
#     }
# }

# print(info)
# print(info["score"]["math"])
# c=info.keys()
# print(c)
# print(len(c))
# s=info.values()
# print(s)
# d=info.items()
# print(d)
# f=info.get("name")
# print(f)
# new_dict={"city":"delhi" ,"age":16}
# info.update(new_dict)
# print(info)

# #SETS
# # duplicate values are not allowed and set is unordered
# col = { 1, 2,2,"j","j"}
# print(col) 
# print(len(col))
# col=set()
# col.add("jatin")
# col.add(1)
# print(col)
# col.remove("jatin")
# print(col)
# col.pop()
# print(col)
# col.clear()
# print(col)

# set1={1,2,3}
# set2={2,3,4}
# print(set1.union(set2))
# print(set1.intersection(set2))

# dict={}
# dict["cat"] = "small animal"
# dict["table"] = ["a piece of furniture","list of facts and figures"]
# print(dict)

# col1 = {"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(col1))

class Solution:
    def twoSum(self, nums:list[int] , target:int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


