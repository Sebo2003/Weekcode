class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None 

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def top(self):
        if not self.is_empty():
            return self.peek()
        else:
            return None
        
    def print(self):
        print("Stack:", self.items)

class Demo:
    def showStack(self) -> None:
        stack = Stack()

        stack.push(5)
        stack.push(-2)
        stack.push(7)

        size = stack.size()

        for i in range(size):
            stack.pop()
        

        for i in range(5):
            stack.push(i+1)
        

        top = stack.top()

        top -= 5

        print(top)

        print(stack.top())
        print(stack.peek())

        if(stack.is_empty == True):
            return None
        elif(stack.is_empty == False):
            stack.push(100)

        stack.print()
        
        for i in range(stack.size()):
            stack.pop()
        
        stack.print()
        
        return None
    
if __name__ == "__main__":
    d = Demo()
    d.showStack()