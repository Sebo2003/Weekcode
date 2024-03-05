class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def print(self):
        print("Queue: ", self.items)
        
class Demo:
    def showStack(self) -> None:
        queue = Queue()

        queue.enqueue(9)
        queue.enqueue(-7)
        queue.enqueue(16)

        size = queue.size()

        for i in range(size):
            queue.dequeue()
        
        for i in range(5):
            queue.enqueue(i+1)
        
        front = queue.front()
        rear = queue.rear()

        front -= 5
        
        rear += 5

        queue.dequeue()

        print("front: ", queue.front())
        print("rear: ", queue.rear())

        if(queue.is_empty == True):
            return None
        elif(queue.is_empty == False):
            queue.enqueue(100)

        queue.print()

        for i in range(queue.size()):
            queue.dequeue()

        queue.print()
        
        return None
    
if __name__ == "__main__":
    d = Demo()
    d.showStack()