from queue import LifoQueue
stack = LifoQueue()
stack.put('A')
stack.put('B')
stack.put('C')
print(stack) #it will get store but it will not print 
print(stack.get())