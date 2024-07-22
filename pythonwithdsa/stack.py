# #implementing stack as list
# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)

# print("Initial stack")
# print(stack)

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print('\n stack after elements are popped:')
# print(stack)

# #implementing stack as deque
# from collections import deque

# stack = deque()
# stack.append(1)
# stack.append(2)
# stack.append(3)

# print("initial stack :")
# print(stack)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack)

#implement stack using lifo queue module 
from queue import LifoQueue

stack = LifoQueue(maxsize=5)
stack.put(1)
stack.put(2)
stack.put(3)
print(stack)

print(stack.qsize())
print(stack.full())

print(stack.get())
print(stack.get())
print(stack.get())
print(stack)
