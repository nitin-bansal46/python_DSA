# Stack abstract data type  with Arrays[list]
# Three nmain function Push, Pop, Peek
# It follows LIFO structure

class Stack:

    def __init__(self):
        self.stack = []

    def isEmtpy(self):
        return self.stack == []

    def Push(self, data):
        self.stack.append(data)

    def Pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def Peek(self):
        data = self.stack[-1]
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)

    def seeStack(self):
        return self.stack

Mystack = Stack()

Mystack.Push(1)
Mystack.Push(20)
Mystack.Push(30)

print(Mystack.seeStack())

print(Mystack.sizeStack())


