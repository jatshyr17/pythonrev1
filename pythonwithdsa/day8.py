
from array import *
l=[]
l.append(11)
print(l)
l.append(2)
print(l)
l.insert(2,"jatin")
print(l)
l.insert(1,4)
l.insert(2,6)
print(l)
l.reverse()
print(l)
l.remove("jatin")
print(l)
l.sort(reverse = True)
print(l)
s = array('i',[1,3,5,7,9])
print(str(s.itemsize))

# (extra concepts)Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents. Also, find the size of the memory buffer in bytes???

# array_num = array('i', [1, 3, 5, 7, 9])
# print("Original array: "+str(array_num))
# print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
# print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))

l = array('i',[1,2,3,4,5])
l.extend(l)
print(l)

l = []
s=array('i',[1,2,6,-8])
s.extend(l)
print(s)
s.insert(1,4)
print(s)
s.pop(1)
print(s)

l.extend(s)
print(l)



